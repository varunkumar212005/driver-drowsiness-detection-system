import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh

def distance(p1, p2):
    return math.dist(p1, p2)

camera = cv2.VideoCapture(0)
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

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        status = "NORMAL"

        if results.multi_face_landmarks:
            face = results.multi_face_landmarks[0]
            h, w, _ = frame.shape

            upper = face.landmark[13]
            lower = face.landmark[14]
            left = face.landmark[78]
            right = face.landmark[308]

            p1 = (int(upper.x * w), int(upper.y * h))
            p2 = (int(lower.x * w), int(lower.y * h))
            p3 = (int(left.x * w), int(left.y * h))
            p4 = (int(right.x * w), int(right.y * h))

            mar = distance(p1, p2) / distance(p3, p4)

            if mar > 0.6:
                yawn_frames += 1
            else:
                yawn_frames = 0

            if yawn_frames >= 15:
                status = "YAWNING DETECTED"

            cv2.putText(frame, f"MAR: {mar:.2f}",
                        (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 0), 2)

        cv2.putText(frame, status, (30, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2)

        cv2.imshow("Driver Yawning Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()
