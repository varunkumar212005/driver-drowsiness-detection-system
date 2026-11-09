def calculate_risk(drowsiness=False, yawning=False, distraction=False,
                    phone=False, alcohol=False, tilt=False):

    risk = 0

    if drowsiness:
        risk += 30

    if yawning:
        risk += 15

    if distraction:
        risk += 25

    if phone:
        risk += 30

    if alcohol:
        risk += 40

    if tilt:
        risk += 20

    risk = min(risk, 100)

    if risk <= 30:
        status = "NORMAL"
    elif risk <= 60:
        status = "WARNING"
    else:
        status = "DANGER"

    return risk, status
