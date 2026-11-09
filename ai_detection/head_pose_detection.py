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

        if results.multi_face_landmarks:
            face = results.multi_face_landmarks[0]

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

            success, rotation, translation = cv2.solvePnP(
                MODEL_POINTS,
                image_points,
                camera_matrix,
                distortion
            )

            if success:
                angles, _, _, _, _, _ = cv2.RQDecomp3x3(
                    cv2.Rodrigues(rotation)[0]
                )

                pitch, yaw, roll = angles

                if abs(yaw) > 20 or abs(pitch) > 20:
                    status = "DISTRACTION ALERT"

                cv2.putText(
                    frame,
                    f"Yaw: {yaw:.1f} Pitch: {pitch:.1f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

        cv2.putText(
            frame,
            status,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255) if status != "NORMAL" else (0, 255, 0),
            2
        )

        cv2.imshow("Head Movement Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
