'use strict';

var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password987',
  database: 'todo'
});

con.connect(function(err){
  if(err){
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

function getAllTodos(callback){
  con.query('SELECT * FROM todos;', function(err, todos){
    if (err) {
      console.log(err.toString());
      return;
    }
    todos.map(function(item) {
      item.completed = (item.completed === 1);
    });
    callback(todos);
  });
}

function getOneTodo(id, callback){
  con.query('SELECT * FROM todos WHERE id = ?', id, function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    callback(todo[0]);
  });
}

function addTodo(text, callback){
  con.query('INSERT INTO todos SET text = ?', text, function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    callback({id: todo.insertId, text: text});
  });
}

function updateTodo(id, completed, callback){
  var completedStatusInDb = completed ? 1 : 0;
  con.query('UPDATE todos SET completed = ? WHERE id = ?', [completedStatusInDb, id], function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    callback({id: id, completed: completed});
  });
}

function deleteTodo(id, callback){
  con.query('DELETE FROM todos WHERE id = ?', id, function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    callback({id: id, destroyed: true})
  });
}

module.exports = {
  getAllTodos: getAllTodos,
  getOneTodo: getOneTodo,
  addTodo: addTodo,
  updateTodo: updateTodo,
  deleteTodo: deleteTodo
}
