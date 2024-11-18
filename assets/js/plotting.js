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

plotData("data.json", "myChart", "bar");
