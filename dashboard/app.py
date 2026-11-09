from flask import Flask, render_template, jsonify, request
from esp32_serial import get_sensor_data, start_serial

app = Flask(__name__)

ai_data = {
    "status": "NORMAL",
    "risk": 0,
    "alerts": []
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/sensors")
def sensors():
    data = get_sensor_data()
    data.update(ai_data)
    return jsonify(data)


@app.route("/api/ai-status", methods=["POST"])
def update_ai_status():
    global ai_data

    received_data = request.get_json()

    if received_data:
        ai_data.update(received_data)

    return jsonify({"message": "AI status updated"})


@app.route("/api/status")
def status():
    return jsonify(ai_data)


if __name__ == "__main__":
    start_serial()
    app.run(host="127.0.0.1", port=5000, debug=False)
