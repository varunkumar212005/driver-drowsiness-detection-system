# Testing Documentation

## Project Title
IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

## 1. Introduction

Testing is performed to verify the functionality of individual modules and the integration of AI, IoT hardware and the web dashboard.

## 2. AI Module Testing

| Test Case | Expected Result |
|---|---|
| Eye closure | Drowsiness alert |
| Continuous yawning | Yawning alert |
| Unusual head movement | Distraction alert |
| Mobile phone detection | Phone detection alert |
| Normal facial behaviour | No AI alert |

## 3. IoT Module Testing

| Test Case | Expected Result |
|---|---|
| Alcohol sensor reading above threshold | Alcohol condition detected |
| Tilt sensor activation | Tilt condition detected |
| Emergency button pressed | Emergency condition detected |
| Normal sensor readings | Normal ESP32 status |
| GPS signal available | Latitude and longitude received |

## 4. Dashboard Testing

| Test Case | Expected Result |
|---|---|
| Open dashboard | Dashboard loads |
| AI data received | AI status displayed |
| ESP32 connected | Connection displayed |
| Sensor data received | Sensor values updated |
| GPS coordinates received | Location displayed |
| Google Maps link selected | Location opens in Maps |

## 5. Integration Testing

1. Verify camera and AI detection.
2. Verify ESP32 sensor readings.
3. Verify GPS communication.
4. Verify AI-to-Flask communication.
5. Verify ESP32-to-Python communication.
6. Verify combined risk assessment.
7. Verify dashboard updates.

## 6. Test Results

Record actual test results after running the complete system.

Do not mark a test as successful until it has been performed.

## 7. Conclusion

Testing helps identify errors and verify the communication between the AI module, IoT hardware and web dashboard.
