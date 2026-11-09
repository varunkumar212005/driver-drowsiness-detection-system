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

    ai_risk = int(ai_data.get("risk", 0))
    alcohol = int(data.get("alcohol", 0))
    tilt = int(data.get("tilt", 0))
    button = int(data.get("button", 0))

    alerts = list(ai_data.get("alerts", []))

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
        "ai_status": ai_data.get("status", "NORMAL"),
        "status": status,
        "risk": risk,
        "alerts": alerts
    })

    return jsonify(data)


@app.route("/api/ai-status", methods=["POST"])
def update_ai_status():

    global ai_data

    received_data = request.get_json()

    if received_data:
        ai_data.update(received_data)

    return jsonify({
        "message": "AI status updated"
    })


@app.route("/api/status")
def status():
    return jsonify(ai_data)


if __name__ == "__main__":
    start_serial()
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
