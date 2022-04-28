
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

//function val(dropdown)
//{
//    var selected = document.getElementById(dropdown).value;
//    console.log(selected);
//}

function dropdownAthlete()
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
let dropdown = document.getElementById('dropdownAthlete')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

for (var i = 0; i < teamData.data.players.length; i++)
{
    option = document.createElement("option");
    let first = teamData.data.players[i].first_name;
    let last  = teamData.data.players[i].last_name;
    option.text = first.concat(" ", last);
    dropdown.appendChild(option);
}
}

function dropdownPosition()
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
let dropdown = document.getElementById('dropdownPosition')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

for (var i = 0; i < teamData.data.players.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.data.players[i].role;
    dropdown.appendChild(option);
}
var usedNames = {};
$("select[name='position'] > option").each(function () {
    if(usedNames[this.text]) {
        $(this).remove();
    } else {
        usedNames[this.text] = this.value;
    }
});

}

window.onload = function()
{
    let btn = document.getElementById("dropdown");
//    let athBtn = document.getElementById("dropdownAthlete");
//    let posBtn = document.getElementById("dropdownPosition");
    dropdown();
    btn.onclick = dropdownAthlete(), dropdownPosition();
}

//////////////////////////////////////////////////////////////////////
//
//function sumDropDown()
//{
//var teamData;
//$.ajax({
//    async: false,
//    url: 'http://localhost:8000/api/dropdown/team/',
//    success: function(data)
//    {
//        teamData = data;
//    }
//});
//let dropdown = document.getElementById('sumDropDown')
//let option;
//while(dropdown.firstChild)
//{
//    dropdown.removeChild(dropdown.firstChild);
//}
//
//for (var i = 0; i < teamData.data.length; i++)
//{
//    option = document.createElement("option");
//    option.text = teamData.data[i].name;
//    dropdown.appendChild(option);
//}
//}
//
//function val()
//{
//    var selected = document.getElementById('sumDropDown').value;
//
//}
//
//window.onload = function()
//{
//    let btn = document.getElementById("sumDropDown");
//    btn.onclick = dropdown;
//}
//
///////////////////////////////////////////////////////////////////////
//
//function inNamedropdown()
//{
//var teamData;
//$.ajax({
//    async: false,
//    url: 'http://localhost:8000/api/dropdown/',
//    success: function(data)
//    {
//        teamData = data;
//    }
//});
//let dropdown = document.getElementById('inNamedropdown')
//let option;
//while(dropdown.firstChild)
//{
//    dropdown.removeChild(dropdown.firstChild);
//}
//
//for (var i = 0; i < teamData.data.length; i++)
//{
//    option = document.createElement("option");
//    option.text = teamData.data[i].name;
//    dropdown.appendChild(option);
//}
//}
//
//function val()
//{
//    var selected = document.getElementById('inNamedropdown').value;
//
//}
//
//window.onload = function()
//{
//    let btn = document.getElementById("inNamedropdown");
//    btn.onclick = dropdown;
//}

