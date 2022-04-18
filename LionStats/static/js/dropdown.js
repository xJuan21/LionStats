//var PythonShell = require('python-shell');

function dropdown()
{
import {PythonShell} from 'python-shell'
var data;
PythonShell.run('teamdropdown', null, function (err, results)
{
    data = results;
    console.log(data);
});

let dropdown = document.getElementById('select')
let option;
for (let i = 0; i < data.length; i++)
{
    option = document.createElement('option');
    option.text = data[i];
    dropdown.add(option);
}
}

let bttn = document.getElementById("teamDropdown");
bttn.addEventListener("click", dropdown, false);

//document.getElementById("teamDropdown").onclick = dropdown;
//let dropdown = $('#menu');
//
//dropdown.empty();
//
//$.each(data, function(key, entry)
//{
//    dropdown.append($('<li><a></a></li>').attr('value', entry.team).text(entry.team));
//})

