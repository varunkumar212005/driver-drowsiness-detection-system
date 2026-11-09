async function updateDashboard() {

    try {

        const response = await fetch("/api/sensors");

        if (!response.ok) {
            throw new Error("Unable to fetch sensor data");
        }

        const data = await response.json();

        const status = document.getElementById("status");

        status.innerText = data.status || "NORMAL";
        status.className = "value";
        status.style.color = "";

        if (data.status === "NORMAL") {

            status.classList.add("normal");

        } else if (data.status === "WARNING") {

            status.style.color = "#facc15";

        } else {

            status.classList.add("danger");
        }

        document.getElementById("risk").innerText =
            (data.risk ?? 0) + "/100";

        document.getElementById("alerts").innerText =
            data.alerts?.length
                ? data.alerts.join(", ")
                : "No Alerts";

        document.getElementById("alcohol").innerText =
            data.alcohol ?? 0;

        document.getElementById("tilt").innerText =
            data.tilt === 1 ? "DETECTED" : "NORMAL";

        document.getElementById("button").innerText =
            data.button === 1 ? "PRESSED" : "NOT PRESSED";

        document.getElementById("connection").innerText =
            data.connected ? "CONNECTED" : "DISCONNECTED";

        document.getElementById("gps").innerText =
            data.gps_valid ? "GPS CONNECTED" : "WAITING FOR GPS";

        document.getElementById("latitude").innerText =
            data.latitude ?? "--";

        document.getElementById("longitude").innerText =
            data.longitude ?? "--";

        document.getElementById("systemInfo").innerText =
            data.connected
                ? "Monitoring Active"
                : "Waiting for ESP32 Connection";

        const mapsLink = document.getElementById("mapsLink");

        if (data.gps_valid && data.maps_link) {

            mapsLink.href = data.maps_link;
            mapsLink.innerText = "View Driver Location";

        } else {

            mapsLink.href = "#";
            mapsLink.innerText = "Location unavailable";
        }

    } catch (error) {

        console.log("Dashboard update error:", error);

        document.getElementById("systemInfo").innerText =
            "Dashboard Connection Error";
    }
}

setInterval(updateDashboard, 1000);

updateDashboard();
