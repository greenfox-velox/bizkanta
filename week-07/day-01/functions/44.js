'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function minElement(numbers) {
  var minimal = numbers[0];
  numbers.forEach(function(e) {
    if (e < minimal) {
      minimal = e;
    }
  });
  return minimal;
}

console.log(minElement(numbers));
