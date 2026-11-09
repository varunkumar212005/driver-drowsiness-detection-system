import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]


def calculate_ear(eye):

    vertical1 = math.dist(eye[1], eye[5])
    vertical2 = math.dist(eye[2], eye[4])
    horizontal = math.dist(eye[0], eye[3])

    if horizontal == 0:
        return 0

    return (vertical1 + vertical2) / (2.0 * horizontal)


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

closed_frames = 0

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

            left = [
                (
                    int(face.landmark[i].x * w),
                    int(face.landmark[i].y * h)
                )
                for i in LEFT_EYE
            ]

            right = [
                (
                    int(face.landmark[i].x * w),
                    int(face.landmark[i].y * h)
                )
                for i in RIGHT_EYE
            ]

            ear = (
                calculate_ear(left) +
                calculate_ear(right)
            ) / 2

            if ear < 0.22:
                closed_frames += 1
            else:
                closed_frames = 0

            if closed_frames >= 20:
                status = "DROWSINESS ALERT"

            cv2.putText(
                frame,
                f"EAR: {ear:.2f}",
                (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 255, 0),
                2
            )

        else:
            closed_frames = 0
            status = "FACE NOT DETECTED"

        color = (
            (0, 0, 255)
            if status == "DROWSINESS ALERT"
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
            "Driver Drowsiness Detection",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()
