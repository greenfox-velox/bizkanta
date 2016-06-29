'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortestString(list) {
  var shortest = list[0];
  list.forEach(function(string) {
    if (string.length < shortest.length) {
      shortest = string;
    }
  });
  return shortest;
}

console.log(shortestString(names));
