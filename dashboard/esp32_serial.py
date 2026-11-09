import serial
import threading

SERIAL_PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200

sensor_data = {
    "alcohol": 0,
    "tilt": 0,
    "button": 0,
    "status": "NORMAL"
}

def read_esp32():
    global sensor_data

    try:
        esp = serial.Serial(
            SERIAL_PORT,
            BAUD_RATE,
            timeout=1
        )

        while True:
            line = esp.readline().decode(
                "utf-8", errors="ignore"
            ).strip()

            if not line:
                continue

            values = {}

            for item in line.split(","):
                if ":" in item:
                    key, value = item.split(":", 1)
                    values[key.strip()] = value.strip()

            if "ALCOHOL" in values:
                sensor_data["alcohol"] = int(values["ALCOHOL"])

            if "TILT" in values:
                sensor_data["tilt"] = int(values["TILT"])

            if "BUTTON" in values:
                sensor_data["button"] = int(values["BUTTON"])

            if "STATUS" in values:
                sensor_data["status"] = values["STATUS"]

    except Exception as error:
        print("ESP32 Error:", error)

def start_serial():
    thread = threading.Thread(
        target=read_esp32,
        daemon=True
    )
    thread.start()

def get_sensor_data():
    return sensor_data.copy()
