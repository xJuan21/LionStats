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
//empty dropdown before populating
let dropdown = document.getElementById('dropdown')
let option;
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

//function for populating athlete dropdown
function dropdownAthlete()
{
var teamData;
//use ajax to get the data from the django rest framework into javascript
$.ajax({
    async: false,
    url: 'http://localhost:8000/api/dropdown/team',
    success: function(data)
    {
        teamData = data;
    }
});
//empty dropdown before populating
let dropdown = document.getElementById('dropdownAthlete')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

var lst = [];
//populate dropdown with data recieved
for (var i = 0; i < teamData.data.players.length; i++)
{
    option = document.createElement("option");
    let first = teamData.data.players[i].first_name;
    let last  = teamData.data.players[i].last_name;
    let pos = teamData.data.players[i].role;
    option.text = first.concat(" ", last, " (", pos, ")")
    dropdown.appendChild(option);
}
}



window.onload = function()
{
    //on page load populate the team dropdown
    let btn = document.getElementById("dropdown");
    dropdown();
    //when the team dropdown is clicked populate the athlete dropdown
    btn.onclick = function(){dropdownAthlete();};
}