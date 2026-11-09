import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh


def distance(p1, p2):
    return math.dist(p1, p2)


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

yawn_frames = 0

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while True:

        success, frame = camera.read()

        if not success:
            break

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = face_mesh.process(rgb)

        status = "NORMAL"

        if results.multi_face_landmarks:

            face = results.multi_face_landmarks[0]

            h, w, _ = frame.shape

            upper = face.landmark[13]
            lower = face.landmark[14]
            left = face.landmark[78]
            right = face.landmark[308]

            p1 = (upper.x * w, upper.y * h)
            p2 = (lower.x * w, lower.y * h)
            p3 = (left.x * w, left.y * h)
            p4 = (right.x * w, right.y * h)

            mouth_width = distance(p3, p4)

            if mouth_width > 0:

                mar = distance(p1, p2) / mouth_width

            else:
                mar = 0

            if mar > 0.6:
                yawn_frames += 1
            else:
                yawn_frames = 0

            if yawn_frames >= 15:
                status = "YAWNING DETECTED"

            cv2.putText(
                frame,
                f"MAR: {mar:.2f}",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

        else:
            yawn_frames = 0
            status = "FACE NOT DETECTED"

        color = (
            (0, 0, 255)
            if status == "YAWNING DETECTED"
            else (0, 255, 0)
        )

        cv2.putText(
            frame,
            status,
            (30, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

        cv2.imshow(
            "Driver Yawning Detection",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()
