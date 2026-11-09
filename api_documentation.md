# API Documentation

## Project
IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

## 1. Overview

The Flask backend provides API endpoints for communication between the AI detection module, ESP32 sensor module and web dashboard.

## 2. API Endpoints

### GET /

Purpose:
Loads the driver monitoring dashboard.

Response:
Displays the dashboard interface.

### POST /api/ai-status

Purpose:
Receives AI detection information from the Python AI module.

Example JSON request:

{
    "status": "WARNING",
    "risk": 30,
    "alerts": ["DROWSINESS"]
}

### GET /api/sensors

Purpose:
Provides combined AI and ESP32 sensor information to the dashboard.

Example JSON response:

{
    "alcohol": 500,
    "tilt": 0,
    "button": 0,
    "connected": true,
    "latitude": 12.345678,
    "longitude": 75.123456,
    "gps_valid": true,
    "status": "NORMAL",
    "risk": 0,
    "alerts": []
}

The values above are illustrative examples, not live sensor readings.

### GET /api/status

Purpose:
Returns the latest AI detection information.

## 3. ESP32 Serial Communication

Baud Rate: 115200

The ESP32 sends sensor information through USB serial communication.

Example:

ALCOHOL:500,TILT:0,BUTTON:0,STATUS:NORMAL,LAT:12.345678,LNG:75.123456,GPS:1

## 4. Communication Flow

1. AI module sends detection results using HTTP POST.
2. ESP32 sends sensor information through serial communication.
3. Python reads and processes serial information.
4. Flask combines AI and IoT information.
5. Dashboard requests updated information using GET /api/sensors.

## 5. Dashboard Update

JavaScript periodically requests sensor information from Flask and updates the dashboard.

Update interval: 1 second.

## 6. Notes

- The Flask server and AI module must run on the same computer for the current localhost API configuration.
- ESP32 must be connected through the configured serial port.
- GPS coordinates are available only when a valid GPS fix is received.
- API responses and hardware communication must be tested before final demonstration.
