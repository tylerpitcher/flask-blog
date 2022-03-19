// Configuration object for bar chart.
var config = {
    type: 'bar',
    data: {
        datasets: [
            {
                label: 'Comments',
                fill: true,
                borderColor: '#00CAFF',
                borderWidth: '1',
                backgroundColor: 'rgba(0, 202, 255, 0.2)',
                lineTension: 0.3
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: 'Top-performing Posts'
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                grid: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Number of Comments'
                }
            },
            x: {
                grid: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Post ID'
                }
            }
        }
    }
};

// Displays chart in dashboard.
function displayChart(labels, data) {
    // Set labels & data values
    config.data.labels = labels;
    config.data.datasets[0].data = data;


    // Create new chart
    new Chart(
        document.getElementById('linechart').getContext('2d'), 
        config
    );
}