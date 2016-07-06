'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count

var fs = require('fs');

function wordCount(filename, cb) {
  fs.readFile(filename, function(err, content) {
    if (err) {
      return cb(err);
    }
    // var count = String(content).split(/\s/g).length;
    var count = String(content).replace('\r\n', ' ').split(' ').length;
    cb(null, count);
  });
}

wordCount('alma.txt', function(err, c) {
  console.log(err, c);
})


//
//
// function count(err, rawContent) {
//   var count = String(rawContent).split(' ').length;
//   console.log(count);
// }
//
// countWords('alma.txt');
