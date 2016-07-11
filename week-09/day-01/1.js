'use strict';

var http = require('http');

var now = new Date();

var server = http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end(req.method + '\n' + req.url + '\n' + now);
});


server.listen(3000, '127.0.0.1');
