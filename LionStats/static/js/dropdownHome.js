//function for populating team dropdown
function dropdown()
{
var teamData;
//use ajax to get the data from the django rest framework into javascript
$.ajax({
    async: false,
    url: 'http://localhost:8000/api/dropdown/',
    success: function(data)
    {
        teamData = data;
    }
});
let dropdown = document.getElementById('dropdown')
let option;
//empty dropdown before populating
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

//create and append empty option to dropdown
option = document.createElement("option");
option.value = "";
dropdown.appendChild(option);

//populate dropdown with data recieved
for (var i = 0; i < teamData.data.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

window.onload = function()
{
    //when the team dropdown is clicked begin populating chart on home page
    let btn = document.getElementById("dropdown");
    dropdown();

    btn.onchange = async function(){
    //populate chart
    $.get("http://localhost:8000/api/home",function(data) {

    var endpoint = '/api/home'
    var teamData = []
    var labels = []
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        //get labels and metric data and use in chart
        labels = data.labels
        teamData = data.default
    const ctx = document.getElementById('stat1').getContext('2d');
    const stat1 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: data.labels,
        datasets: [{
            data: teamData,
            backgroundColor: [
                'rgba(253, 181, 37, 0.7)',
                'rgba(253, 181, 37, 0.4)',
                'rgba(253, 181, 37, 0.7)',
                'rgba(253, 181, 37, 0.4)',
                'rgba(253, 181, 37, 0.7)',
                'rgba(253, 181, 37, 0.4)',
                'rgba(253, 181, 37, 0.7)',
                'rgba(253, 181, 37, 0.4)',
                'rgba(253, 181, 37, 0.7)',
            ],
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
})
}
    });
});
}
}

