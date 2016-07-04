'use strict';


var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];


// create a function that counts all the books of an array of students
// not every student has a property called books

function countBooks(students) {
  var count = 0;
  students.forEach(function(e) {
    count += (e.books && e.books.length) || 0;
  });
  return count;
}

console.log(countBooks(students));

module.exports.countBooks = countBooks;
