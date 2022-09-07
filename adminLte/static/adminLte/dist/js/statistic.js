
// const DATA_COUNT = 7;
// const NUMBER_CFG = {count: DATA_COUNT, min: -100, max: 100};

const labels = ['mon', 'thu', 'wed', 'the', 'fri'];
let data_line;
data_line = {
    labels: labels,
    datasets: [
        {
            label: 'Dataset 1',
            data: [700, 500, 400, 600, 300],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgb(255,182,197)',
        }]
}
const configLine = {
    type: 'line',
    data: data_line,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            }
        }
    },
};
var $visitorsChart = $('#visitors-chart')

var visitorsChart = new Chart($visitorsChart,configLine)

var donutData = {
    labels: [
        'Chrome',
        'IE',
        'FireFox',
        'Safari',
        'Opera',
        'Navigator',
    ],
    datasets: [
        {
            data: [700, 500, 400, 600, 300, 100],
            backgroundColor: ['#f56954', '#00a65a', '#f39c12', '#00c0ef', '#3c8dbc', '#d2d6de'],
        }
    ]
}
//-------------
//- PIE CHART -
//-------------
// Get context with jQuery - using jQuery's .get() method.
var pieChartCanvas = $('#pieChart').get(0).getContext('2d')
var pieData = donutData;
var pieOptions = {
    maintainAspectRatio: false,
    responsive: true,
}
//Create pie or douhnut chart
// You can switch between pie and douhnut using the method below.
new Chart(pieChartCanvas, {
    type: 'pie',
    data: pieData,
    options: pieOptions
})