import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

while True:

    success, frame = camera.read()

    if not success:
        print("Error: Unable to read camera frame.")
        break

    results = model(frame, verbose=False)

    status = "NORMAL"

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            if model.names[class_id] == "cell phone" and confidence >= 0.40:

                status = "PHONE DETECTED"

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    frame,
                    f"Phone: {confidence:.2f}",
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

    color = (0, 0, 255) if status == "PHONE DETECTED" else (0, 255, 0)

    cv2.putText(
        frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    cv2.imshow(
        "Mobile Phone Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
