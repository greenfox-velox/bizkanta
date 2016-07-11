'use strict';

var express = require('express');

var app = express();

var todos = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
]

app.get('/todos/', function(req, res) {
  res.send(todos);
});

function getOneTodo(todoItem) {
  for (var i = 0; i < todos.length; i++) {
    if (parseInt(todos[i].id) === parseInt(todoItem)) {
      return todos[i];
    }
  }
}

app.get('/todos/:id', function(req, res) {
  res.send(getOneTodo(req.params.id));
});

app.listen(3000);
