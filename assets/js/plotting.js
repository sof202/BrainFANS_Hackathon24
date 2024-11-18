async function fetchData() {
    const response = await fetch(
        "https://api.github.com/repos/octocat/Hello-World/stargazers",
    );
    const data = await response.json();
    return data.length; // Number of stargazers
}

async function plotData() {
    const stargazersCount = await fetchData();
    const ctx = document.getElementById("myChart").getContext("2d");
    const myChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Stargazers"],
            datasets: [{
                label: "# of Stars",
                data: [stargazersCount],
                backgroundColor: "rgba(75, 192, 192, 0.2)",
                borderColor: "rgba(75, 192, 192, 1)",
                borderWidth: 1,
            }],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}

plotData();
