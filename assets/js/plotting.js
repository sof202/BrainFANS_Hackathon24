function plotData(dataset, chartID, chartType) {
    fetch(dataset)
        .then((response) => response.json())
        .then((data) => {
            const ctx = document.getElementById(chartID).getContext("2d");
            const myChart = new Chart(ctx, {
                type: chartType,
                data: data,
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                color: "white",
                            },
                            grid: {
                                color: "rgba(200, 200, 200, 0.2)",
                            },
                        },
                        x: {
                            beginAtZero: true,
                            ticks: {
                                color: "white",
                            },
                            grid: {
                                color: "rgba(200, 200, 200, 0.2)",
                            },
                        },
                    },
                    plugins: {
                        legend: {
                            labels: {
                                color: "white",
                                font: "outfit",
                            },
                        },
                    },
                },
            });
        })
        .catch((error) => console.error("Error fetching the data:", error));
}

plotData("lines_changed.json", "lines_changed", "bar");
plotData("pull_requests_closed.json", "closed_prs", "bar");
plotData("collaborative_pull_requests.json", "collaborative_prs", "bar");
plotData("issues_worked_on.json", "issues_worked_on", "bar");
