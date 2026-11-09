# IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

A final-year BE Computer Science and Engineering project developed at SDM Institute of Technology, Ujire.

This project combines Artificial Intelligence, Computer Vision and Internet of Things (IoT) to monitor driver behaviour, detect potentially unsafe conditions and display real-time safety information through a web dashboard.

## PROJECT OVERVIEW

The system uses a camera and ESP32-based hardware to monitor driver alertness and identify dangerous driving conditions.

It combines AI-based facial analysis, mobile phone detection, alcohol sensing, vehicle tilt detection and GPS tracking.

## KEY FEATURES

1. Drowsiness Detection using Eye Aspect Ratio (EAR).
2. Yawning Detection using Mouth Aspect Ratio (MAR).
3. Distraction Detection using head-pose estimation.
4. Mobile Phone Detection using YOLO.
5. Alcohol Detection using MQ-3 sensor.
6. Vehicle Tilt Detection using a tilt sensor.
7. Emergency Alert using a push button.
8. GPS Tracking using NEO-6M GPS module.
9. Alert System using buzzer and LEDs.
10. Live Web Dashboard using Flask.

## TECHNOLOGIES USED

Software:
- Python
- OpenCV
- MediaPipe
- NumPy
- YOLO
- Flask
- HTML
- CSS
- JavaScript
- PySerial

Hardware:
- ESP32 DevKit V1
- MQ-3 Alcohol Sensor
- Tilt Sensor
- NEO-6M GPS Module
- Buzzer
- Green LED
- Yellow LED
- Red LED
- Push Button

## PROJECT STRUCTURE

driver-drowsiness-detection-system/

ai_detection/
    main.py
    eye_detection.py
    yawning_detection.py
    head_pose_detection.py
    phone_detection.py
    risk_assessment.py
    test_risk_assessment.py

dashboard/
    app.py
    esp32_serial.py
    templates/
        index.html
    static/
        css/
            style.css
        js/
            dashboard.js

esp32/
    driver_monitor.ino

datasets/
models/
docs/
screenshots/

requirements.txt
.gitignore
README.md

## SYSTEM ARCHITECTURE

1. AI-Based Driver Monitoring

The camera captures the driver's face. Python processes the video using OpenCV and MediaPipe. YOLO is used for mobile phone detection.

2. IoT-Based Sensor Monitoring

The ESP32 collects information from the MQ-3 alcohol sensor, tilt sensor, emergency button and GPS module. It controls the LEDs and buzzer based on sensor conditions.

3. Web Dashboard

The Flask application receives AI information and ESP32 sensor readings. The dashboard displays the driver's status, risk score, alerts and GPS coordinates.

## ESP32 PIN CONNECTIONS

MQ-3 Sensor - GPIO 34
Tilt Sensor - GPIO 4
Emergency Button - GPIO 23
Buzzer - GPIO 18
Green LED - GPIO 25
Red LED - GPIO 14
Yellow LED - GPIO 26
GPS RX - GPIO 16
GPS TX - GPIO 17

GPS communication uses ESP32 Serial2.

Note: Check voltage requirements before connecting hardware. ESP32 GPIO pins are not 5 V tolerant.

## AI DETECTION METHODS

Eye Closure - MediaPipe - Eye Aspect Ratio
Yawning - MediaPipe - Mouth Aspect Ratio
Head Movement - OpenCV - Head Pose Estimation
Phone Detection - YOLO - Object Detection
Risk Assessment - Python - Weighted Risk Scoring

## RISK ASSESSMENT

Drowsiness - 30 points
Yawning - 15 points
Distraction - 25 points
Phone Detection - 30 points
Alcohol Detection - 40 points
Vehicle Tilt - 20 points

The risk score is capped at 100.

Driver Status:

NORMAL: 0-30
WARNING: 31-60
DANGER: 61-100

An emergency button press also triggers DANGER status.

These are prototype settings and require calibration and testing.

## INSTALLATION AND SETUP

Requirements:
- Python 3
- Arduino IDE
- ESP32 board support
- VS Code
- USB cable
- ESP32 hardware and required sensors

Step 1: Clone the Repository

git clone https://github.com/varunkumar212005/driver-drowsiness-detection-system.git

cd driver-drowsiness-detection-system

Step 2: Create Virtual Environment

python3 -m venv venv

Activate on macOS/Linux:

source venv/bin/activate

Activate on Windows:

venv\Scripts\activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Configure ESP32

1. Install ESP32 board support in Arduino IDE.
2. Install TinyGPS++ library.
3. Open esp32/driver_monitor.ino.
4. Select the appropriate ESP32 board and port.
5. Upload the firmware.

Step 5: Start Flask Dashboard

cd dashboard

python app.py

Step 6: Start AI Detection

Open another terminal:

cd ai_detection

python main.py

Open the dashboard in your browser:

http://127.0.0.1:5000

The AI application and Flask dashboard should run on the same computer.

## GPS TRACKING

The NEO-6M GPS module communicates with ESP32 through UART.

The ESP32 sends GPS latitude and longitude through serial communication. Python reads these values and generates a Google Maps location link.

GPS coordinates may take time to become available, especially indoors or where satellite reception is weak.

## DASHBOARD INFORMATION

The dashboard is designed to display:

- Driver safety status
- Combined risk score
- AI detection alerts
- Alcohol sensor readings
- Tilt sensor status
- Emergency button status
- ESP32 connection status
- GPS connection status
- Latitude and longitude
- Google Maps location link

## PROJECT OBJECTIVES

1. Develop an AI-based driver drowsiness detection system.
2. Identify yawning and distracted driving behaviour.
3. Detect mobile phone usage through object detection.
4. Integrate IoT sensors for monitoring unsafe conditions.
5. Implement GPS-based location tracking.
6. Develop a real-time web dashboard.
7. Combine AI and IoT information for driver risk assessment.

## ACADEMIC DETAILS

Institution: SDM Institute of Technology, Ujire

Programme: BE Computer Science and Engineering

Project Type: Final Year Major Project

Project Title: IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

## PROJECT TEAM

- Pavanakumar
- Samhitha S Rao
- Tejas SR
- Varun Kumar M

## FUTURE ENHANCEMENTS

1. SMS-based emergency notifications.
2. Cloud-based monitoring and data storage.
3. Improved AI model accuracy.
4. Historical driver behaviour analysis.
5. Mobile application integration.
6. Real-time location sharing.

## DISCLAIMER

This project is developed for academic and demonstration purposes. It is a prototype and is not a certified vehicle safety system. Detection accuracy, sensor calibration and hardware reliability must be evaluated before any real-world application.

## LICENSE

This is an academic team project. Licensing and reuse permissions should be agreed upon by the project team.
