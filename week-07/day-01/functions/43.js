'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function filterOdds(numbers) {
  var newArray = [];
  numbers.forEach(function(e) {
    if (e % 2 === 0) {
      newArray.push(e);
    };
  });
  return newArray;
}

console.log(filterOdds(numbers));
