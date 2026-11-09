import cv2
import mediapipe as mp
import math
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

mp_face_mesh = mp.solutions.face_mesh

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def distance(p1, p2):
    return math.dist(p1, p2)

def calculate_ear(points):
    return (
        distance(points[1], points[5]) +
        distance(points[2], points[4])
    ) / (2 * distance(points[0], points[3]))

camera = cv2.VideoCapture(0)

closed_frames = 0
yawn_frames = 0

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

        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb)

        status = "NORMAL"
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
                alerts.append("DROWSINESS")

            upper = face.landmark[13]
            lower = face.landmark[14]
            left = face.landmark[78]
            right = face.landmark[308]

            p1 = (upper.x * w, upper.y * h)
            p2 = (lower.x * w, lower.y * h)
            p3 = (left.x * w, left.y * h)
            p4 = (right.x * w, right.y * h)

            mar = distance(p1, p2) / distance(p3, p4)

            if mar > 0.6:
                yawn_frames += 1
            else:
                yawn_frames = 0

            if yawn_frames >= 15:
                alerts.append("YAWNING")

            cv2.putText(
                frame,
                f"EAR: {ear:.2f} MAR: {mar:.2f}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 0),
                2
            )

        detections = model(frame, verbose=False)

        for result in detections:
            for box in result.boxes:

                class_id = int(box.cls[0])

                if model.names[class_id] == "cell phone":

                    alerts.append("PHONE DETECTED")

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

        if alerts:
            status = "WARNING"

        cv2.putText(
            frame,
            status,
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255) if alerts else (0, 255, 0),
            2
        )

        for index, alert in enumerate(alerts):
            cv2.putText(
                frame,
                alert,
                (20, 115 + index * 30),
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
