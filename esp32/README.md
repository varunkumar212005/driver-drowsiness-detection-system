# ESP32 IoT Hardware Module

This module connects IoT sensors and hardware components to the IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System.

### 1. Hardware Components

- ESP32 DevKit V1
- MQ-3 Alcohol Sensor
- NEO-6M GPS Module
- Tilt Sensor
- Buzzer
- Green LED
- Yellow LED
- Red LED
- Push Button
- Breadboard
- Jumper Wires

### 2. GPIO Pin Configuration

| Component | ESP32 GPIO |
|---|---|
| MQ-3 Sensor Analog Output | GPIO 34 |
| Tilt Sensor | GPIO 4 |
| Push Button | GPIO 23 |
| Buzzer | GPIO 18 |
| Green LED | GPIO 25 |
| Red LED | GPIO 14 |
| Yellow LED | GPIO 26 |
| GPS RX (ESP32 receives) | GPIO 16 |
| GPS TX (ESP32 transmits) | GPIO 17 |

### 3. Features

- Alcohol detection
- Vehicle tilt detection
- GPS location tracking
- Emergency button
- Buzzer alerts
- LED status indication
- Serial communication with Python dashboard
- Real-time sensor data monitoring

### 4. Software Requirements

- Arduino IDE
- ESP32 board support package
- TinyGPS++ library

### 5. Firmware

The main ESP32 firmware is available in:

`driver_monitor.ino`

The firmware performs the following operations:

- Reads alcohol sensor values.
- Detects vehicle tilt.
- Monitors the emergency button.
- Reads GPS coordinates.
- Controls the buzzer and LED indicators.
- Sends sensor information to the Python dashboard through serial communication.

### 6. Serial Communication

- USB Serial Baud Rate: 115200
- GPS Baud Rate: 9600
- Communication Protocol: Serial UART

### 7. GPS Configuration

The NEO-6M GPS module communicates with the ESP32 using UART2.

- GPS TX connects to ESP32 GPIO 16.
- GPS RX connects to ESP32 GPIO 17.
- GPS provides latitude and longitude information.
- Location information is forwarded to the dashboard.

### 8. Alert System

NORMAL:
- Green LED indication.

WARNING:
- Yellow warning indication is planned for the dashboard.

DANGER:
- Red LED indication.
- Buzzer activation.
- Dashboard danger notification.

### 9. Safety Notes

- ESP32 GPIO pins are not 5V tolerant.
- Ensure the MQ-3 analog output voltage is within the ESP32 ADC input range.
- Use a suitable regulated power supply.
- Check all connections before powering the circuit.
- Verify the sensor wiring before testing.

### 10. Purpose

The ESP32 module monitors physical driving conditions and sends sensor and GPS information to the main driver monitoring application.

This module works together with the AI detection system to provide a combined driver monitoring solution.
