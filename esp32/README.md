ESP32 IoT HARDWARE MODULE

This module connects IoT sensors and hardware components to the driver monitoring system.

1. HARDWARE COMPONENTS

ESP32 DevKit V1
MQ-3 Alcohol Sensor
NEO-6M GPS Module
Tilt Sensor
Buzzer
Green LED
Yellow LED
Red LED
Push Button
Breadboard and jumper wires

2. GPIO PIN CONFIGURATION

MQ-3 Sensor Analog Output - GPIO 34
Tilt Sensor - GPIO 4
Push Button - GPIO 23
Buzzer - GPIO 18
Green LED - GPIO 25
Red LED - GPIO 14
Yellow LED - GPIO 26
GPS RX (ESP32 receives) - GPIO 16
GPS TX (ESP32 transmits) - GPIO 17

3. FEATURES

Alcohol detection
Vehicle tilt detection
GPS location tracking
Emergency button
Buzzer alerts
LED status indication
Serial communication with Python dashboard

4. SOFTWARE REQUIREMENTS

Arduino IDE
ESP32 board support
TinyGPS++ library

5. FIRMWARE

The main ESP32 firmware is available in:

driver_monitor.ino

It reads sensor values, processes GPS information, controls the buzzer and LEDs, and sends data to the Python dashboard through serial communication.

6. SERIAL COMMUNICATION

Baud Rate: 115200
GPS Baud Rate: 9600
Communication: USB Serial

7. SAFETY NOTES

ESP32 GPIO pins are not 5V tolerant.
Ensure the MQ-3 analog output voltage is within the ESP32 ADC input range.
Use a suitable regulated power supply.
Check all connections before powering the circuit.

8. PURPOSE

The ESP32 module monitors physical driving conditions and sends sensor and GPS information to the main driver monitoring application.
