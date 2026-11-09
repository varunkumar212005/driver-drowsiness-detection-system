# System Architecture

## Project Title
IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

## 1. Overview

The system combines Artificial Intelligence, Computer Vision and Internet of Things to monitor driver behaviour and identify potentially unsafe driving conditions.

## 2. Main Components

### AI Monitoring Module
- Captures video using a camera.
- Detects eye closure using EAR.
- Detects yawning using MAR.
- Estimates head pose to identify distraction.
- Detects mobile phones using YOLO.
- Calculates the AI risk score.

### IoT Monitoring Module
- ESP32 collects sensor readings.
- MQ-3 detects alcohol-related sensor readings.
- Tilt sensor detects vehicle tilting.
- Push button triggers an emergency condition.
- GPS module provides location coordinates.
- LEDs and buzzer indicate safety conditions.

### Web Dashboard
- Flask provides the backend API.
- Python receives ESP32 serial data.
- JavaScript updates dashboard information.
- HTML and CSS provide the user interface.
- GPS coordinates generate a Google Maps link.

## 3. Data Flow

1. Camera captures driver video.
2. AI module processes facial features and detects unsafe behaviour.
3. AI module sends detection information to Flask.
4. ESP32 collects hardware sensor readings.
5. Python receives sensor readings through USB serial communication.
6. Flask combines AI and IoT information.
7. Risk score and driver status are calculated.
8. Dashboard displays the updated information.

## 4. Communication

- Camera to AI: Video processing.
- AI to Flask: HTTP POST API.
- ESP32 to Python: USB serial communication.
- Python to Flask: Sensor data.
- Flask to Dashboard: HTTP JSON API.
- ESP32 to GPS: UART communication.

## 5. Expected Output

The system displays three driver conditions:

NORMAL – No major unsafe condition detected.

WARNING – Elevated risk detected.

DANGER – High risk or emergency condition detected.

## 6. Future Scope

- Emergency SMS notifications.
- Cloud-based data storage.
- Mobile application integration.
- Improved detection accuracy.
- Historical driver behaviour analysis.
