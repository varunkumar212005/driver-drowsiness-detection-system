#define MQ3_PIN 34
#define TILT_PIN 4
#define BUTTON_PIN 23

#define BUZZER_PIN 18
#define GREEN_LED 25
#define RED_LED 14
#define YELLOW_LED 26

String status = "NORMAL";

void setup() {
    Serial.begin(115200);

    pinMode(MQ3_PIN, INPUT);
    pinMode(TILT_PIN, INPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);

    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(GREEN_LED, OUTPUT);
    pinMode(RED_LED, OUTPUT);
    pinMode(YELLOW_LED, OUTPUT);

    Serial.println("Driver Monitoring System Started");
}

void loop() {
    int alcoholValue = analogRead(MQ3_PIN);
    int tiltValue = digitalRead(TILT_PIN);
    int buttonValue = digitalRead(BUTTON_PIN);

    bool alcoholDetected = alcoholValue > 2000;
    bool tiltDetected = tiltValue == HIGH;
    bool emergencyPressed = buttonValue == LOW;

    if (alcoholDetected || tiltDetected || emergencyPressed) {
        status = "DANGER";
    }
    else {
        status = "NORMAL";
    }

    digitalWrite(GREEN_LED, status == "NORMAL");
    digitalWrite(RED_LED, status == "DANGER");
    digitalWrite(YELLOW_LED, LOW);

    digitalWrite(BUZZER_PIN, status == "DANGER");

    Serial.print("ALCOHOL:");
    Serial.print(alcoholValue);

    Serial.print(",TILT:");
    Serial.print(tiltDetected);

    Serial.print(",BUTTON:");
    Serial.print(emergencyPressed);

    Serial.print(",STATUS:");
    Serial.println(status);

    delay(500);
}
