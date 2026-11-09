# AI Models

This folder stores AI models used in the IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System.

### 1. Models Used

- YOLOv8n: Used for real-time object detection and mobile phone detection.
- MediaPipe Face Mesh: Used to identify facial landmarks.
- Eye Aspect Ratio (EAR): Used for detecting eye closure and drowsiness.
- Mouth Aspect Ratio (MAR): Used for detecting yawning.
- Head Pose Estimation: Used for detecting driver head movement and distraction.

### 2. Technologies

- YOLO
- OpenCV
- MediaPipe
- Python
- NumPy
- Ultralytics

### 3. Model Files

- yolov8n.pt: Pretrained YOLO model.
- best.pt: Custom trained model (optional, future use).

The YOLOv8n model can be downloaded automatically by the Ultralytics library when required.

### 4. Purpose

The AI models help detect driver drowsiness, yawning, mobile phone usage and distraction in real time.

### 5. Future Improvements

- Train a custom phone detection model.
- Improve detection accuracy.
- Perform model evaluation and testing.
- Optimize real-time detection performance.
- Calibrate detection thresholds.

### 6. Note

The models and detection thresholds must be tested and calibrated before real-world use. This project is developed as an academic prototype.
