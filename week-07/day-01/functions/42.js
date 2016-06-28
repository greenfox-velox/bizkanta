'use strict';

// create a function that returns it's input factorial
function factorial(num) {
  var number = 1;
  for (var i = 2; i < num + 1; i++) {
    number *= i;
  }
  return number;
}

console.log(factorial(4));
