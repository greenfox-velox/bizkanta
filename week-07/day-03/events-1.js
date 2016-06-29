'use strict';
// Turn the party on and off by clicking the button.
var button = document.querySelector('button');
var div = document.querySelector('div');

function partyTime () {
  div.classList.toggle('party');
}

button.addEventListener('click', partyTime);
