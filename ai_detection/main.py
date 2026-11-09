import cv2
import mediapipe as mp
import math
import numpy as np
import json
import time
import urllib.request

from ultralytics import YOLO
from risk_assessment import calculate_risk

model = YOLO("yolov8n.pt")

mp_face_mesh = mp.solutions.face_mesh

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

LANDMARKS = [1, 152, 33, 263, 61, 291]

MODEL_POINTS = np.array([
    (0, 0, 0),
    (0, -330, -65),
    (-225, 170, -135),
    (225, 170, -135),
    (-150, -150, -125),
    (150, -150, -125)
], dtype=np.float64)


def distance(p1, p2):
    return math.dist(p1, p2)


def calculate_ear(points):
    horizontal = distance(points[0], points[3])

    if horizontal == 0:
        return 0

    return (
        distance(points[1], points[5]) +
        distance(points[2], points[4])
    ) / (2 * horizontal)


camera = cv2.VideoCapture(0)

closed_frames = 0
yawn_frames = 0
last_api_update = 0
frame_count = 0
phone_detected = False

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while camera.isOpened():

        success, frame = camera.read()

        if not success:
            break

        frame_count += 1

        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb)

        drowsiness = False
        yawning = False
        distraction = False
        phone = phone_detected

        alerts = []

        if results.multi_face_landmarks:

            face = results.multi_face_landmarks[0]

            left_eye = [
                (int(face.landmark[i].x * w),
                 int(face.landmark[i].y * h))
                for i in LEFT_EYE
            ]

            right_eye = [
                (int(face.landmark[i].x * w),
                 int(face.landmark[i].y * h))
                for i in RIGHT_EYE
            ]

            ear = (
                calculate_ear(left_eye) +
                calculate_ear(right_eye)
            ) / 2

            if ear < 0.22:
                closed_frames += 1
            else:
                closed_frames = 0

            if closed_frames >= 20:
                drowsiness = True
                alerts.append("DROWSINESS")

            upper = face.landmark[13]
            lower = face.landmark[14]
            left = face.landmark[78]
            right = face.landmark[308]

            p1 = (upper.x * w, upper.y * h)
            p2 = (lower.x * w, lower.y * h)
            p3 = (left.x * w, left.y * h)
            p4 = (right.x * w, right.y * h)

            mouth_width = distance(p3, p4)

            mar = (
                distance(p1, p2) / mouth_width
                if mouth_width > 0 else 0
            )

            if mar > 0.6:
                yawn_frames += 1
            else:
                yawn_frames = 0

            if yawn_frames >= 15:
                yawning = True
                alerts.append("YAWNING")

            image_points = np.array([
                (face.landmark[i].x * w,
                 face.landmark[i].y * h)
                for i in LANDMARKS
            ], dtype=np.float64)

            focal_length = w
            center = (w / 2, h / 2)

            camera_matrix = np.array([
                [focal_length, 0, center[0]],
                [0, focal_length, center[1]],
                [0, 0, 1]
            ], dtype=np.float64)

            distortion = np.zeros((4, 1))

            pose_success, rotation, translation = cv2.solvePnP(
                MODEL_POINTS,
                image_points,
                camera_matrix,
                distortion
            )

            if pose_success:

                angles, _, _, _, _, _ = cv2.RQDecomp3x3(
                    cv2.Rodrigues(rotation)[0]
                )

                pitch, yaw, roll = angles

                if abs(yaw) > 20 or abs(pitch) > 20:
                    distraction = True
                    alerts.append("DISTRACTION")

                cv2.putText(
                    frame,
                    f"Yaw: {yaw:.1f} Pitch: {pitch:.1f}",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 0),
                    2
                )

            cv2.putText(
                frame,
                f"EAR: {ear:.2f} MAR: {mar:.2f}",
                (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 0),
                2
            )

        else:
            closed_frames = 0
            yawn_frames = 0

        if frame_count % 3 == 0:

            detections = model(frame, verbose=False)

            phone_detected = False

            for result in detections:
                for box in result.boxes:

                    class_id = int(box.cls[0])

                    if model.names[class_id] == "cell phone":

                        phone_detected = True

                        x1, y1, x2, y2 = map(
                            int, box.xyxy[0]
                        )

                        cv2.rectangle(
                            frame,
                            (x1, y1),
                            (x2, y2),
                            (0, 0, 255),
                            2
                        )

        phone = phone_detected

        if phone:
            alerts.append("PHONE DETECTED")

        risk, status = calculate_risk(
            drowsiness=drowsiness,
            yawning=yawning,
            distraction=distraction,
            phone=phone
        )

        if time.time() - last_api_update >= 1:

            data = {
                "status": status,
                "risk": risk,
                "alerts": alerts
            }

            try:
                payload = json.dumps(data).encode("utf-8")

                api_request = urllib.request.Request(
                    "http://127.0.0.1:5000/api/ai-status",
                    data=payload,
                    headers={
                        "Content-Type": "application/json"
                    },
                    method="POST"
                )

                with urllib.request.urlopen(
                    api_request,
                    timeout=2
                ) as response:
                    response.read()

            except Exception as error:
                print("Dashboard connection error:", error)

            last_api_update = time.time()

        color = (0, 255, 0)

        if status == "WARNING":
            color = (0, 255, 255)

        elif status == "DANGER":
            color = (0, 0, 255)

        cv2.putText(
            frame,
            f"STATUS: {status}",
            (20, 105),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

        cv2.putText(
            frame,
            f"RISK SCORE: {risk}/100",
            (20, 140),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        for index, alert in enumerate(alerts):

            cv2.putText(
                frame,
                alert,
                (20, 180 + index * 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        cv2.imshow(
            "AI Driver Monitoring System",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()
