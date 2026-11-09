from flask import Flask, jsonify, render_template
from esp32_serial import get_sensor_data, start_serial

app = Flask(name)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/sensors")
def sensors():
    return jsonify(get_sensor_data())

@app.route("/api/status")
def status():
    data = get_sensor_data()

    return jsonify({
        "status": data["status"],
        "alcohol": data["alcohol"],
        "tilt": data["tilt"],
        "button": data["button"]
    })

if name == "main":
    start_serial()
    app.run(host="127.0.0.1", port=5000, debug=False)
