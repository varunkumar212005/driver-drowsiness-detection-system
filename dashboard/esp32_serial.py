import serial
import threading
import time
import os

SERIAL_PORT = os.getenv(
    "ESP32_PORT",
    "/dev/cu.usbserial-0001"
)

BAUD_RATE = 115200

sensor_data = {
    "alcohol": 0,
    "tilt": 0,
    "button": 0,
    "esp32_status": "DISCONNECTED",
    "connected": False
}

data_lock = threading.Lock()
serial_thread = None


def read_esp32():
    global sensor_data

    while True:
        try:
            print("Connecting to ESP32...")

            esp = serial.Serial(
                SERIAL_PORT,
                BAUD_RATE,
                timeout=1
            )

            with data_lock:
                sensor_data["connected"] = True
                sensor_data["esp32_status"] = "CONNECTED"

            print("ESP32 Connected Successfully!")

            while True:
                line = esp.readline().decode(
                    "utf-8",
                    errors="ignore"
                ).strip()

                if not line:
                    continue

                values = {}

                for item in line.split(","):
                    if ":" in item:
                        key, value = item.split(":", 1)
                        values[key.strip()] = value.strip()

                with data_lock:

                    if "ALCOHOL" in values:
                        sensor_data["alcohol"] = int(
                            values["ALCOHOL"]
                        )

                    if "TILT" in values:
                        sensor_data["tilt"] = int(
                            values["TILT"]
                        )

                    if "BUTTON" in values:
                        sensor_data["button"] = int(
                            values["BUTTON"]
                        )

                    if "STATUS" in values:
                        sensor_data["esp32_status"] = (
                            values["STATUS"]
                        )

        except Exception as error:

            print("ESP32 Error:", error)

            with data_lock:
                sensor_data["connected"] = False
                sensor_data["esp32_status"] = "DISCONNECTED"

            time.sleep(3)


def start_serial():
    global serial_thread

    if serial_thread and serial_thread.is_alive():
        return

    serial_thread = threading.Thread(
        target=read_esp32,
        daemon=True
    )

    serial_thread.start()


def get_sensor_data():
    with data_lock:
        return sensor_data.copy()
