async function updateDashboard() {
    try {
        const response = await fetch("/api/sensors");

        if (!response.ok) {
            throw new Error("Unable to fetch sensor data");
        }

        const data = await response.json();

        const status = document.getElementById("status");

        status.innerText = data.status;

        status.className = "value " +
            (data.status === "NORMAL" ? "normal" : "danger");

        document.getElementById("alcohol").innerText = data.alcohol;

        document.getElementById("tilt").innerText =
            data.tilt == 1 ? "DETECTED" : "NORMAL";

        document.getElementById("button").innerText =
            data.button == 1 ? "PRESSED" : "NOT PRESSED";

    } catch (error) {
        console.error("Dashboard Error:", error);
    }
}

updateDashboard();

setInterval(updateDashboard, 1000);
