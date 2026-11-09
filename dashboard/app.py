from flask import Flask, render_template, jsonify, request
from esp32_serial import get_sensor_data, start_serial
import threading

app = Flask(__name__)

ai_data = {
    "status": "NORMAL",
    "risk": 0,
    "alerts": []
}

ai_lock = threading.Lock()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/sensors")
def sensors():

    data = get_sensor_data()

    with ai_lock:
        current_ai_data = ai_data.copy()

    ai_risk = int(current_ai_data.get("risk", 0))
    ai_risk = max(0, min(ai_risk, 100))

    alcohol = int(data.get("alcohol", 0))
    tilt = int(data.get("tilt", 0))
    button = int(data.get("button", 0))

    alerts = list(current_ai_data.get("alerts", []))

    risk = ai_risk

    if alcohol > 2000:
        risk += 40
        alerts.append("ALCOHOL DETECTED")

    if tilt == 1:
        risk += 20
        alerts.append("VEHICLE TILT DETECTED")

    if button == 1:
        alerts.append("EMERGENCY BUTTON PRESSED")

    risk = min(risk, 100)

    if button == 1 or risk > 60:
        status = "DANGER"

    elif risk > 30:
        status = "WARNING"

    else:
        status = "NORMAL"

    data.update({
        "ai_status": current_ai_data.get("status", "NORMAL"),
        "status": status,
        "risk": risk,
        "alerts": alerts
    })

    return jsonify(data)


@app.route("/api/ai-status", methods=["POST"])
def update_ai_status():

    received_data = request.get_json(silent=True)

    if not isinstance(received_data, dict):
        return jsonify({
            "error": "Invalid AI data"
        }), 400

    try:

        risk = int(received_data.get("risk", 0))

        if not 0 <= risk <= 100:
            raise ValueError

        status = received_data.get("status", "NORMAL")

        if status not in ["NORMAL", "WARNING", "DANGER"]:
            raise ValueError

        alerts = received_data.get("alerts", [])

        if not isinstance(alerts, list):
            raise ValueError

        with ai_lock:

            ai_data.update({
                "status": status,
                "risk": risk,
                "alerts": alerts
            })

    except (ValueError, TypeError):

        return jsonify({
            "error": "Invalid AI values"
        }), 400

    return jsonify({
        "message": "AI status updated successfully"
    })


@app.route("/api/status")
def status():

    with ai_lock:
        return jsonify(ai_data.copy())


if __name__ == "__main__":

    start_serial()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
