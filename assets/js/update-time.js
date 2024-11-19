fetch("update_time.txt")
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("update-time").innerText = data;
    })
    .catch((error) => {
        console.error("Error fetching the text file:", error);
        document.getElementById("update-time").innerText =
            "Failed to load update time.";
    });
