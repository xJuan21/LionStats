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
    let first = teamData.data.players[i].first_name;
    let last  = teamData.data.players[i].last_name;
    let pos = teamData.data.players[i].role;
    let combo = first.concat(" ", last, " (", pos, ")")
    lst.push(combo);
}

//create a multiselect dropdown
$(document).ready(function() {
var select2 = $('#dropdownAthlete').select2({
    placeholder: "Select",
    width: '500px',
    data:lst,
    multiple: true,
    closeOnSelect: false,
})

select2.trigger("change");
});
}

//function for populating position dropdown
function dropdownPosition()
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
let dropdown = document.getElementById('dropdownPosition')
let option;
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

//populate dropdown with data recieved
for (var i = 0; i < teamData.data.players.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.data.players[i].role;
    dropdown.appendChild(option);
}
//delete duplicates
var usedNames = {};
$("select[name='position'] > option").each(function () {
    if(usedNames[this.text]) {
        $(this).remove();
    } else {
        usedNames[this.text] = this.value;
    }
});

}

//function for populating session dropdown
function dropdownSession()
{
var teamData;
//use ajax to get the data from the django rest framework into javascript
$.ajax({
    async: false,
    url: 'http://localhost:8000/api/dropdown/sessions',
    success: function(data)
    {
        teamData = data;
    }
});
let dropdown = document.getElementById('dropdownSession')
let option;
//empty dropdown before populating
while(dropdown.firstChild)
{
    dropdown.removeChild(dropdown.firstChild);
}

//populate dropdown with data recieved
for (var i = 0; i < teamData.date.length; i++)
{
    option = document.createElement("option");
    option.text = teamData.date[i];
    dropdown.appendChild(option);
}
}

window.onload = function()
{
    let btn = document.getElementById("dropdown");
    let sessionBtn = document.getElementById("sessionBtn");

    dropdown();
    //when the team dropdown is clicked populate the athlete and position function
    btn.onclick = function(){dropdownAthlete(); dropdownPosition();};
    //when the session btn is clicked populate session dropdown
    sessionBtn.onclick = function(){dropdownSession();};
}
