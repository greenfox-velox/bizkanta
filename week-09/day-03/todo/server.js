'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var dbQueries = require('./db_queries');

var app = express();

var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());
app.use(express.static('./'));

app.get('/todos/', function(req, res) {
  dbQueries.getAllTodos(function(todos){
    res.send(todos);
  });
});

app.get('/todos/:id', function(req, res) {
  dbQueries.getOneTodo(req.params.id, function(todos){
    res.send(todos);
  });
});

app.post('/todos/', urlencodedParser, function(req, res) {
  dbQueries.addTodo(req.body.text, function(todo){
    res.send(todo);
  });
});

app.put('/todos/:id', urlencodedParser, function(req, res) {
  var id = req.params.id;
  var completed = req.body.completed;
  dbQueries.updateTodo(id, completed, function(todo){
    res.send(todo);
  });
});

app.delete('/todos/:id', urlencodedParser, function(req, res) {
  var id = req.params.id;
  dbQueries.deleteTodo(id, function(todo){
    res.send(todo);
  });
});

var port = 3000;
app.listen(port, function(){
  console.log('I am listening on port ' + port);
});
