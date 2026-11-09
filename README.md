# IoT and AI-Powered Driver Drowsiness and Distraction Detection System

A final-year BE Computer Science and Engineering project that combines computer vision, AI, and IoT hardware to monitor driver alertness and identify potentially unsafe driving conditions.

## Project overview

The planned system combines:
- **Camera-based monitoring:** OpenCV and MediaPipe Face Mesh for facial-landmark analysis.
- **Drowsiness indicators:** Eye Aspect Ratio (EAR), mouth opening / yawning analysis, and head movement.
- **Distraction detection:** YOLO-based mobile-phone detection (add the trained model to `models/` when ready).
- **IoT monitoring:** ESP32 integration with alcohol and tilt sensors, buzzer, LEDs, push button, and GPS module.
- **Dashboard:** A Flask-based interface for displaying detection status, risk level, sensor information, and event logs.

> Project status: Repository starter structure. Replace the placeholders with your tested source code and update this README as each module is integrated. Do not claim a feature is complete until it has been tested.

## Repository structure

```text
.
├── ai_detection/       # Python computer-vision and AI modules
├── dashboard/          # Flask dashboard, templates, and static assets
├── esp32/              # ESP32 Arduino firmware
├── docs/               # Report, diagrams, and technical documentation
├── datasets/            # Dataset notes; avoid committing large/raw datasets
├── models/              # Trained model files; large weights may need Git LFS
├── screenshots/         # Dashboard and prototype screenshots
├── requirements.txt
└── README.md
```

## Getting started

1. Install Python 3.10 or a compatible version supported by your dependencies.
2. Create and activate a virtual environment:

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add the project source files to their corresponding folders.
5. Configure camera, model, serial-port, and dashboard settings according to your hardware.
6. Run the entry-point script documented by your implementation.

## Hardware

The prototype is designed around an ESP32 development board and may include:
- NEO-6M GPS module
- MQ-3 alcohol sensor
- Tilt / vibration sensor
- Buzzer and status LEDs
- Push button
- USB connection to the computer

Check voltage levels and the ESP32 board's input limits before wiring. Do not connect a 5 V signal directly to an ESP32 GPIO/ADC pin unless the circuit safely scales it to an acceptable level.

## Detection approach

- Facial landmarks are used to estimate eye and mouth measurements.
- EAR can help identify prolonged eye closure.
- Mouth-opening measurements can help identify yawning.
- Head-pose / movement analysis can contribute to distraction detection.
- A YOLO model can be used to detect a phone in the camera frame.
- Sensor and AI events can be combined into a risk state such as `NORMAL`, `WARNING`, or `DANGER`.

Thresholds must be calibrated and evaluated with suitable test data. This project is an academic prototype, not a certified driver-safety device.

## Team and academic details

- **Institution:** SDM Institute of Technology, Ujire
- **Programme:** BE Computer Science and Engineering
- **Project:** IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

Add team-member names, guide details, datasets, citations, and test results before final submission.

## Screenshots and demo

Add genuine screenshots to `screenshots/` and link them here. Add a demo video link after publishing the video.

## License

Choose a license before making this repository available for reuse. If this is an academic team project, confirm that all team members agree on the license.
