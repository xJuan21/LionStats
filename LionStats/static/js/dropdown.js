//var PythonShell = require('python-shell');

//function dropdown()
//{
//const {PythonShell} = require('python-shell');
//var data;
//PythonShell.run('teamdropdown', null, function (err, results)
//{
//    data = results;
//    console.log(data);
//});


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

for (var i = 0; i < teamData.data.length; i++)
{
    option = document.createElement("option");
    option.value = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

//function val(dropdown)
//{
//    var selected = document.getElementById(dropdown).value;
//    console.log(selected);
//}

function dropdownTeam()
{
var teamData;
$.ajax({
    async: false,
    url: 'http://localhost:8000/api/dropdown/team',
    success: function(data)
    {
        teamData = data;
    }
});
let dropdown = document.getElementById('dropdownTeam')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

for (var i = 0; i < teamData.data.length; i++)
{
    option = document.createElement("option");
    option.value = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

window.onload = function()
{
    let btn = document.getElementById("dropdown");
    let athBtn = document.getElementById("dropdownTeam");
    btn.onclick = dropdown;
    athBtn.onclick = dropdownTeam;
}

