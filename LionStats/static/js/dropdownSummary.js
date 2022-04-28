
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
$("select[name='summaryPosition'] > option").each(function () {
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

    dropdown();
    btn.onclick = dropdownPosition();
}

