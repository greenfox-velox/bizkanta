'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

var fs = require('fs');

function concatContent(file1, file2, cb) {
  fs.readFile(file1, function(err, content1) {
    if (err) {
      return cb(err);
    }
    fs.readFile(file2, function(err, content2) {
      if (err) {
        return cb(err);
      }
      var concated = String(content1).concat(String(content2));
      cb(null, concated);
    });
  });
}

concatContent('alma.txt', 'writeFileName.txt', function(err, c) {
  console.log(err, c);
})
