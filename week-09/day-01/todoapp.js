'use strict';

var express = require('express');
var bodyParser = require('body-parser');

var app = express();
var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());

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
];

app.get('/todos/', function(req, res) {
  res.send(todos);
});

// get one todo with for loop
//
// function getOneTodo(todoId) {
//   for (var i = 0; i < todos.length; i++) {
//     if (parseInt(todos[i].id) === parseInt(todoId)) {
//       return todos[i];
//     }
//   }
// }

function getOneTodo(todoId) {
  return todos.filter(function(todo) {
    if (parseInt(todo.id) === parseInt(todoId)) {
      return todo;
    }
  });
}

app.get('/todos/:id', function(req, res) {
  var selectedTodo = getOneTodo(req.params.id);
  res.send(selectedTodo);
});

var todoId = 3;

function addOneTodo(text) {
  todoId++;
  var newTodo = {
    "completed": false,
    "id": todoId,
    "text": text,
  };
  todos.push(newTodo);
  // console.log(newTodo);
  return newTodo;
}

app.post('/todos/', urlencodedParser, function(req, res) {
  var newTodo = addOneTodo(req.body.text);
  res.send(newTodo);
});

function modifyTodo(id, text, completed) {
  for (var i = 0; i < todos.length; i++) {
    if (parseInt(todos[i].id) === parseInt(id)) {
      todos[i].completed = completed;
      todos[i].text = text;
      return todos[i];
    }
  }
}

app.put('/todos/:id', urlencodedParser, function(req, res) {
  var modifiedTodo = modifyTodo(req.params.id, req.body.text, req.body.completed);
  res.send(modifiedTodo);
});

function deleteTodo(id) {
  for (var i = 0; i < todos.length; i++) {
    if (parseInt(todos[i].id) === parseInt(id)) {
      todos[i].destroyed = true;
      var removed = todos.splice(i, 1)[0];
      return removed;
    }
  }
}

app.delete('/todos/:id', urlencodedParser, function(req, res) {
  var deletedItem = deleteTodo(req.params.id);
  if (deletedItem) {
    res.send(deletedItem);
  } else {
    res.status(404).json({error: 'id dont exist'});
  }
});

var port = 3000;
app.listen(port, function(){
  console.log('I am listening on port ' + port);
});
