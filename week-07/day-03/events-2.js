'use strict';
// On the click of the button,
// Count the items in the list
// And display the result in the result element.
var button = document.querySelector('button');
var listElements = document.querySelectorAll('li');
var result = document.querySelector('.result');

function countItems () {
  result.textContent = listElements.length;
}

button.addEventListener('click', countItems);
