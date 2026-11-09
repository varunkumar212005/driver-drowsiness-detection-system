import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

LANDMARKS = [1, 152, 33, 263, 61, 291]

MODEL_POINTS = np.array([
    (0, 0, 0),
    (0, -330, -65),
    (-225, 170, -135),
    (225, 170, -135),
    (-150, -150, -125),
    (150, -150, -125)
], dtype=np.float64)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while True:

        ret, frame = camera.read()

        if not ret:
            break

        h, w, _ = frame.shape

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = face_mesh.process(rgb)

        status = "NORMAL"
        color = (0, 255, 0)

        if results.multi_face_landmarks:

            face = results.multi_face_landmarks[0]

            image_points = np.array([
                (
                    face.landmark[i].x * w,
                    face.landmark[i].y * h
                )
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

                rotation_matrix, _ = cv2.Rodrigues(rotation)

                angles, _, _, _, _, _ = cv2.RQDecomp3x3(
                    rotation_matrix
                )

                pitch, yaw, roll = angles

                if abs(yaw) > 20 or abs(pitch) > 20:

                    status = "DISTRACTION DETECTED"
                    color = (0, 0, 255)

                cv2.putText(
                    frame,
                    f"Yaw: {yaw:.1f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2
                )

                cv2.putText(
                    frame,
                    f"Pitch: {pitch:.1f}",
                    (20, 75),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2
                )

        else:
            status = "FACE NOT DETECTED"
            color = (0, 165, 255)

        cv2.putText(
            frame,
            status,
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

        cv2.imshow(
            "Driver Head Pose Detection",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

camera.release()
cv2.destroyAllWindows()
