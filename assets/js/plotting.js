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
