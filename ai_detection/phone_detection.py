import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

while camera.isOpened():
    success, frame = camera.read()

    if not success:
        break

    results = model(frame, verbose=False)

    status = "NORMAL"

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])

            if model.names[class_id] == "cell phone":
                status = "PHONE DETECTED"

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    frame,
                    "Mobile Phone Detected",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255) if status != "NORMAL" else (0, 255, 0),
        2
    )

    cv2.imshow("Mobile Phone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
