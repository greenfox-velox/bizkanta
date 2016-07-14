'use strict';

var express = require('express');
var bodyParser = require('body-parser');
var mysql = require('mysql');
var app = express();

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

var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());
app.use(express.static('./'));

app.get('/todos/', function(req, res) {
  con.query('SELECT * FROM todos;',function(err,todos){
    if(err) {
      console.log(err.toString());
      return;
    }
    todos.map(function(item) {
      item.completed = (item.completed === 1);
    });
    res.send(todos);
  });
});

app.get('/todos/:id', function(req, res) {
  con.query('SELECT * FROM todos WHERE id = ?', req.params.id, function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send(todo[0]);
  });
});

app.post('/todos/', urlencodedParser, function(req, res) {
  con.query('INSERT INTO todos SET text = ?', req.body.text, function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send({id: todo.insertId, text: req.body.text});
  });
});

app.put('/todos/:id', urlencodedParser, function(req, res) {
  var completedStatusInDb = req.body.completed ? 1 : 0;
  con.query('UPDATE todos SET completed = ? WHERE id = ?', [completedStatusInDb, req.params.id], function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send({id: req.params.id, completed: req.body.completed});
  });
});

app.delete('/todos/:id', urlencodedParser, function(req, res) {
  con.query('DELETE FROM todos WHERE id = ?', req.params.id,function(err,todo){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.send({id: req.params.id, destroyed: true});
  });
});

var port = 3000;
app.listen(port, function(){
  console.log('I am listening on port ' + port);
});
