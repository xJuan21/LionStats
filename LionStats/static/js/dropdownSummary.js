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



window.onload = function()
{
    //on page load populate team dropdown
    let btn = document.getElementById("dropdown");
    dropdown();
}