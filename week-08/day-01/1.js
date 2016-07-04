'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}


function countLetters(string) {
  var obj = {};
  var lettersList = string.split('');
  lettersList.forEach(function(e){
    obj[e] = obj[e] + 1 || 1;
  });
  return obj;
}

module.exports.countLetters = countLetters;

// function countLetters(string) {
//   var letter_object = {};
//   var letters_list = string.split('');
//   letters_list.forEach(function(e) {
//     if (!(e in letter_object)) {
//       letter_object[e] = 1;
//     } else {
//       letter_object[e] += 1;
//     }
//   })
//   return letter_object;
// }

// console.log(countLetters('apple'));