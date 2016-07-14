'use strict';

var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;
var express = require('express');
var bodyParser = require('body-parser');
var app = express();

var urlencodedParser = bodyParser.urlencoded({ extended: false });
app.use(bodyParser.json());
app.use(express.static('./'));

// Connection URL. This is where your mongodb server is running.
var url = 'mongodb://localhost:27017/todo';

// Use connect method to connect to the Server
MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

    var collection = db.collection('todo');

    app.get('/todos/', function(req, res) {
      collection.find({}, { 'id': 1, 'text': 1, _id : 0 }).toArray(function (err, result) {
        if (err) {
          console.log(err);
        }
        res.send(result);
      });
    });

    app.get('/todos/:id', function(req, res) {
      collection.find({'id' : parseInt(req.params.id)}, { 'id': 1, 'text': 1, _id : 0 }).toArray(function (err, result) {
        if (err) {
          console.log(err);
        }
        res.send(result);
      });
    });
  app.listen(3000);
  }
});
