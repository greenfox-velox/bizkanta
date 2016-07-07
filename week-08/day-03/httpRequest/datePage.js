'use strict';

function httpRequest() {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    console.log(JSON.parse(xhr.response).weekday);
    console.log(JSON.parse(xhr.response).celebrations.length);
  };
  xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/06')
  xhr.send();
}
var button = document.querySelector('button');

button.addEventListener('click', httpRequest);
