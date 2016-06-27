'use strict';

// Write a program that prints the numbers from 1 to 100.
// But for multiples of three print "Fizz" instead of the number
// and for the multiples of five print "Buzz".
// For numbers which are multiples of both three and five print "FizzBuzz".
for (var i = 1; i <= 100; i++) {
  var printable = '';
  if (i % 3 === 0) {
    printable += 'Fizz';
  } if (i % 5 === 0) {
    printable += 'Buzz';
  } if (printable === '') {
    printable = i;
  }
  console.log(printable);
}
