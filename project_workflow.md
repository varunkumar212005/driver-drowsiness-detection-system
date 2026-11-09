# Project Workflow

## IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

### 1. System Initialization
- Start ESP32.
- Initialize all connected sensors.
- Initialize GPS communication.
- Start the Flask dashboard.
- Initialize the camera and AI models.

### 2. Driver Monitoring
- Capture live video from the camera.
- Detect facial landmarks using MediaPipe.
- Calculate Eye Aspect Ratio (EAR).
- Calculate Mouth Aspect Ratio (MAR).
- Estimate head pose.
- Detect mobile phones using YOLO.

### 3. IoT Sensor Monitoring
- Read alcohol sensor values.
- Read tilt sensor status.
- Monitor emergency button.
- Receive GPS coordinates.

### 4. Risk Assessment
- Calculate AI-based risk score.
- Add IoT-based risk points.
- Determine the overall driver status.
- Generate alerts when unsafe conditions are detected.

### 5. Alert Generation
- NORMAL: Green LED.
- WARNING: Yellow warning indicator.
- DANGER: Red LED and buzzer.

### 6. Dashboard Monitoring
- Send AI information to Flask.
- Receive ESP32 sensor data through serial communication.
- Update the dashboard through JavaScript.
- Display driver status and risk score.
- Display sensor information.
- Display GPS coordinates and Google Maps location.

### 7. Expected Result

The system provides continuous driver monitoring and displays detected safety conditions through the web dashboard.

Note: The complete workflow must be verified through hardware and software testing.
