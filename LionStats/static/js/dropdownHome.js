
function dropdown()
{
var teamData;
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
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

option = document.createElement("option");
option.value = "";
dropdown.appendChild(option);

for (var i = 0; i < teamData.data.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

window.onload = function()
{
    let btn = document.getElementById("dropdown");
    dropdown();

    btn.onchange = async function(){

//    await new Promise(r => setTimeout(r, 5000));
    $.get("http://localhost:8000/api/home",function(data) {

    var endpoint = '/api/home'
    var teamData = []
    var labels = []
    $.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
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

