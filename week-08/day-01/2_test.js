'use strict';

var countBooks = require('./2');
var tape = require('tape');

var students = [
  {name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings']},
  {name: 'Ryan', age: 11, books: ['The funcdation']},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9, books: []},
  {name: 'Jessica', age: 12, books: ['Dune']},
  {name: 'Robert', age: 15}
];

var students2 = [
  {name: 'Steve', age: 12},
  {name: 'Ryan', age: 11},
  {name: 'Sheela', age: 14},
  {name: 'Charlee', age: 9},
  {name: 'Jessica', age: 12},
  {name: 'Robert', age: 15}
];

tape(function(t) {
  t.deepEqual(countBooks.countBooks(students), 4)
  t.deepEqual(countBooks.countBooks(students2), 0)
  t.end();
});
