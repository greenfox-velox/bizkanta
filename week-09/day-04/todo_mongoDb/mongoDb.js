'use strict';

function ConnectToDb(){
  var mongodb = require('mongodb');
  var MongoClient = mongodb.MongoClient;
  var url = 'mongodb://127.0.0.1:27017/todo';
  var that = this;
  MongoClient.connect(url, function (err, db) {
    if (err) {
      console.log('Unable to connect to the mongoDB server. Error:', err);
    } else {
      console.log('Connection established to', url);

      that.collection = db.collection('todo');
    }
  });
}

ConnectToDb.prototype.getAllTodos = function (callback){
  this.collection.find({}, { 'id': 1, 'text': 1, _id : 0 }).toArray(function (err, todos) {
    if (err) {
      console.log(err);
    }
    callback(todos);
  });
}

module.exports = {
  ConnectToDb: ConnectToDb
}
