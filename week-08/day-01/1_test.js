'use strict';

var countLetters = require('./1');
var tape = require('tape');

tape(function(t) {
  t.deepEqual(countLetters.countLetters('apple'), {a: 1, p: 2, l: 1, e: 1});
  t.end();
});
