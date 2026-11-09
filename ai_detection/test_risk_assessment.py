from risk_assessment import calculate_risk


def test_normal_status():
    risk, status = calculate_risk()
    assert risk == 0
    assert status == "NORMAL"


def test_warning_status():
    risk, status = calculate_risk(drowsiness=True)
    assert risk == 30
    assert status == "NORMAL"


def test_danger_status():
    risk, status = calculate_risk(
        drowsiness=True,
        phone=True,
        alcohol=True
    )
    assert risk == 100
    assert status == "DANGER"


if __name__ == "__main__":
    test_normal_status()
    test_warning_status()
    test_danger_status()
    print("All risk assessment tests passed!")
