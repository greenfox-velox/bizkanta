'use strict';

function Xhr_request(){
  this.url = 'http://127.0.0.1:3000/todos/';

  this.getTodosFromServer = function(callback){
    this.createRequest('GET', this.url, null, callback);
  }

  this.addTodoToServer = function(text, callback){
    var newItem = JSON.stringify({'text' : text});
    this.createRequest('POST', this.url, newItem, callback);
  }

  this.deleteTodoFromServer = function(id, callback){
    var url = this.url + id;
    this.createRequest('DELETE', url, null, callback);
  }

  this.completeTodoInServer = function(item, callback){
    var url = this.url + item.id;
    var item = JSON.stringify(item);
    this.createRequest('PUT', url, item, callback);
  }

  this.createRequest = function(method, url, data, callback){
    var xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader('content-type', 'application/json');
    xhr.send(data);
    xhr.onload = function() {
      if (xhr.readyState === xhr.DONE) {
        var response = JSON.parse(xhr.response);
        callback(response);
      };
    };
  }
}
