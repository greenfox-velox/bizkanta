'use strict';
// Remove the king from the list.
var list = document.querySelector('.asteroids');
var king = document.querySelector('li');
list.removeChild(king);
// Add 3 list items saying 'The Fox' to the list.
var fox1 = document.createElement('li');
fox1.textContent = 'The Fox';
list.appendChild(fox1);

var fox2 = document.createElement('li');
fox2.textContent = 'The Fox';
list.appendChild(fox2);

var fox3 = document.createElement('li');
fox3.textContent = 'The Fox';
list.appendChild(fox3);
