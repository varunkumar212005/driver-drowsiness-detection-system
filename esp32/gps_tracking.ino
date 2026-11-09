#include <TinyGPSPlus.h>

TinyGPSPlus gps;

void setup() {
    Serial.begin(115200);
    Serial2.begin(9600, SERIAL_8N1, 16, 17);

    Serial.println("GPS Tracking Started");
}

void loop() {
    while (Serial2.available()) {
        gps.encode(Serial2.read());
    }

    if (gps.location.isUpdated()) {
        double latitude = gps.location.lat();
        double longitude = gps.location.lng();

        Serial.print("LATITUDE:");
        Serial.println(latitude, 6);

        Serial.print("LONGITUDE:");
        Serial.println(longitude, 6);

        Serial.print("GOOGLE MAPS:");
        Serial.print("https://www.google.com/maps?q=");
        Serial.print(latitude, 6);
        Serial.print(",");
        Serial.println(longitude, 6);
    }

    delay(500);
}
