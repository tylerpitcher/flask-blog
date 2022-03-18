const config = {
    type: 'line',
    data: {
        labels: ['A', 'B'],
        datasets: [
            {
                label: 'Points',
                data: [1, 2],
                fill: true,
                borderColor: '#53FF00',
                backgroundColor: 'rgba(83, 255, 0, 0.2)',
                lineTension: 0.1
            }
        ]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                grid: {
                    display: false
                }
            },
            x: {
                grid: {
                    display: false
                }
            }
        }
    }
};

function displayCharts() {
    var ctx1 = document.getElementById('linechart1').getContext('2d');
    var ctx2 = document.getElementById('linechart2').getContext('2d');
    var linechart1 = new Chart(ctx1, config);
    var linechart2 = new Chart(ctx2, config);
}