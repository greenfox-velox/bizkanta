'use strict';

var numbers = [2.4, 3.5, 1.7, 3.3, 1.2];

// create a function that takes an array of numbers,
// it should return a new array that consists only the numbers that are
// bigger than 2 and all of it's elements should be rounded

function biggerThan2(numbers) {
  var newArray = numbers.filter(function(e) {return e > 2});
  return newArray.map(function(e) {return Math.round(e)});
}

console.log(biggerThan2(numbers));
