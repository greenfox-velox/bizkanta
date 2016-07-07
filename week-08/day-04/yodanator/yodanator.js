'use strict';

var inputField = document.querySelector('input')
var button = document.querySelector('button');
var h3 = document.querySelector('h3')
var accessToken = 'O0Y7PdueqlmshuEJv7qM45Zq2l7Ap1RAuZPjsnoDPNhRd9qXJH';
var url = 'https://yoda.p.mashape.com/yoda';

// function display() {
//   h3.textContent = inputField.value;
//   console.log(inputField.value);
// }

function yodanator() {
  var xhr = new XMLHttpRequest();
  var text = inputField.value;
  var response = url + '?sentence=' + encodeURIComponent(text);

  xhr.open('GET', response);
  xhr.setRequestHeader("X-Mashape-Key", accessToken);
  xhr.onload = function() {
    h3.textContent = xhr.response;
  };
  xhr.send();
}

button.addEventListener('click', yodanator);
