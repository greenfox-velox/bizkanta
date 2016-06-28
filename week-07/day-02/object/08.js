'use strict';

var students = [
  {name: 'Rezso', age: 9.5, candies: 2},
  {name: 'Gerzson', age: 10, candies: 1},
  {name: 'Aurel', age: 7, candies: 3},
  {name: 'Zsombor', age: 12, candies: 5},
  {name: 'Olaf', age: 12, candies: 7},
  {name: 'Teodor', age: 3, candies: 2}
];


// create a function that counts the students that
// has more than 4 candies

// with for loop:

// function studentMoreThan4Candies(student_list) {
//   var count = 0;
//   for (var i = 0; i < student_list.length; i++) {
//     if (student_list[i].candies > 4) {
//       count += 1;
//     }
//   }
//   return count;
// }

// with forEach:

function studentMoreThan4Candies(student_list) {
  var count = 0;
  student_list.forEach(function(e) {if (e.candies > 4) {
    count += 1;
    }
  })
  return count;
}

console.log(studentMoreThan4Candies(students));
