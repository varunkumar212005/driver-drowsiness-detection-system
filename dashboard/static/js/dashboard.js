async function updateDashboard() {
    try {
        const response = await fetch("/api/sensors");
        const data = await response.json();

        const status = document.getElementById("status");

        status.innerText = data.status || "NORMAL";

        status.className = "value";

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
            data.alerts && data.alerts.length > 0
                ? data.alerts.join(", ")
                : "No Alerts";

        document.getElementById("alcohol").innerText =
            data.alcohol ?? 0;

        document.getElementById("tilt").innerText =
            data.tilt ?? 0;

        document.getElementById("button").innerText =
            data.button ?? 0;

    } catch (error) {
        console.log("Dashboard update error:", error);
    }
}

setInterval(updateDashboard, 1000);

updateDashboard();
