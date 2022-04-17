//var PythonShell = require('python-shell');
import PythonShell from 'python-shell'
var data;
PythonShell.run('teampro_test.py', null, function (err, results)
{
    data = results;
    console.log(data);
});

let option;
for (let i = 0; i < data)

//let dropdown = $('#menu');
//
//dropdown.empty();
//
//$.each(data, function(key, entry)
//{
//    dropdown.append($('<li><a></a></li>').attr('value', entry.team).text(entry.team));
//})

