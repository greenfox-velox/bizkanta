'use strict';
// Remove the king from the list.
var list = document.querySelector('.asteroids');
var king = document.querySelector('li');
list.removeChild(king);
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']
var newList = ['apple', 'bubble', 'cat', 'green fox'];

newList.forEach(function(e) {
  var newLi = document.createElement('li');
  newLi.textContent = e;
  list.appendChild(newLi);
});
