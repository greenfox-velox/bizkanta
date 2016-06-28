'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10];
// write your own sum function
function sum_of_nums(numbers) {
  var sum = 0;
  for (var i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}
//
// function sum2(numbers) {
//   return numbers.reduce((a, b) => a + b);
// }

console.log(sum_of_nums(numbers));
// console.log(sum2(numbers));
