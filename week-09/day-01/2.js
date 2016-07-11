'use strict';

var express = require('express');

var app = express();
var now = new Date();

app.get('*', function(req, res) {
  res.send(req.method + ' ' + req.url + ' ' + now);
});

app.listen(3000);
