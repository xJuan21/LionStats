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
    option.text = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

function val()
{
    var selected = document.getElementById('dropdown').value;

}

window.onload = function()
{
    let btn = document.getElementById("dropdown");
    btn.onclick = dropdown;
}

////////////////////////////////////////////////////////////////////

function sumDropDown()
{
var teamData;
$.ajax({
    async: false,
    url: 'http://localhost:8000/api/dropdown/team/',
    success: function(data)
    {
        teamData = data;
    }
});
let dropdown = document.getElementById('sumDropDown')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

for (var i = 0; i < teamData.data.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

function val()
{
    var selected = document.getElementById('sumDropDown').value;

}

window.onload = function()
{
    let btn = document.getElementById("sumDropDown");
    btn.onclick = dropdown;
}

/////////////////////////////////////////////////////////////////////

function inNamedropdown()
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
let dropdown = document.getElementById('inNamedropdown')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

for (var i = 0; i < teamData.data.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.data[i].name;
    dropdown.appendChild(option);
}
}

function val()
{
    var selected = document.getElementById('inNamedropdown').value;

}

window.onload = function()
{
    let btn = document.getElementById("inNamedropdown");
    btn.onclick = dropdown;
}

