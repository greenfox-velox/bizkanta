'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise
function isAllPrimes(num_list) {
  return num_list.every(function(e) {return isPrime(e)})
}

function isPrime(number) {
  for (var i = 2; i < number; i++) {
    return number % i !== 0;
  }
  return number > 1
}

console.log(isPrime(7));
console.log(isAllPrimes(numbers));
