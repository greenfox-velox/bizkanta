'use strict';

(function(document, Xhr_request){

  var request = new Xhr_request();

  var inputField = document.querySelector('input');
  var addButton = document.querySelector('.add_button');
  var todoList = document.querySelector('ul');
  addButton.addEventListener('click', newTodoItem);

  request.getTodosFromServer(insertItemsToDOM);

  function insertItemsToDOM(items) {
    items.forEach(function(item) {
      appendTodo(item);
    });
  }

  function newTodoItem(event) {
    event.preventDefault();
    var todoText = inputField.value;
    request.addTodoToServer(todoText, appendTodo);
    inputField.value = '';
    inputField.focus();
  }

  function deleteItemFromDOM(item) {
    document.getElementById(item.id).remove();
  }

  function updateItemInDOM(item) {
    document.getElementById(item.id).classList.toggle('completed');
  }

  function appendTodo(item) {
    if (item.text.length > 0 && item.text.length < 35) {
      var todoItem = document.createElement('li');
      var trashIcon = document.createElement('button');
      var completeIcon = document.createElement('button');
      todoItem.setAttribute('id', item.id);
      todoItem.innerText = item.text;
      todoItem.appendChild(completeIcon);
      todoItem.appendChild(trashIcon);
      completeIcon.classList.add('btn');
      trashIcon.classList.add('btn');
      completeIcon.classList.add('check-button');
      trashIcon.classList.add('trash-button');
      trashIcon.addEventListener('click', trashIconEvent(item))
      if (item.completed) {
        todoItem.classList.add('completed');
      }
      completeIcon.addEventListener('click', function() {
        request.completeTodoInServer({
          id: item.id,
          text: item.text,
          completed: !item.completed,
        }, updateItemInDOM);
      });
      todoList.appendChild(todoItem);
    }
  }

  function trashIconEvent(item) {
    return function(event) {
      request.deleteTodoFromServer(item.id, deleteItemFromDOM);
    }
  }
})(document, Xhr_request);
