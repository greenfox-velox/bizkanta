'use strict';

// Remove the king from the list.
var list = document.querySelector('.asteroids');
var king = document.querySelector('li');
list.removeChild(king);
// Fill the list based on the following list of objects:
var planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]

planetData.forEach(function(e) {
  var newLi = document.createElement('li');
  if (e.asteroid) {
    newLi.textContent = e.content;
    newLi.classList.add(e.category);
    list.appendChild(newLi);
  }
});

// only add the asteroids to the list.
// each list item should have its category as a class
// and its content as text content.
