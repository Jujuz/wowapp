var http= require('http');
var fs = require('fs');
var index = fs.readFileSync('index.html');

var server = http.createServer(function (reququest, response) {
    console.log('testing');
    response.end(index);
});



server.listen(3000);