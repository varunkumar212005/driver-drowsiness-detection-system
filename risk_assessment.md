# Risk Assessment Documentation

## Project Title
IoT and AI-Powered Real-Time Driver Drowsiness and Distraction Detection System

## 1. Introduction

The risk assessment module combines AI detection results and IoT sensor readings to calculate the overall driver risk score.

## 2. Risk Score Allocation

| Detection | Risk Points |
|---|---:|
| Drowsiness | 30 |
| Yawning | 15 |
| Distraction | 25 |
| Phone Detection | 30 |
| Alcohol Detection | 40 |
| Vehicle Tilt | 20 |

## 3. Risk Calculation

The risk points from detected conditions are added together.

Maximum risk score: 100.

The final score cannot exceed 100.

## 4. Driver Status Classification

NORMAL: 0–30

WARNING: 31–60

DANGER: 61–100

An emergency button press directly triggers DANGER status.

## 5. Example

Suppose the system detects:

Drowsiness: 30 points

Yawning: 15 points

Phone Detection: 30 points

Total Risk Score: 75/100

Driver Status: DANGER

## 6. Alert System

NORMAL:
- Green LED indicator.

WARNING:
- Yellow dashboard warning indicator.

DANGER:
- Red LED indicator.
- Buzzer activation.
- Dashboard danger notification.

## 7. Conclusion

The risk assessment module combines multiple detection results to provide an overall indication of potentially unsafe driving conditions.

The scoring thresholds are prototype settings and require testing and calibration.
