'use strict';

var rectangle = require('./3');
var tape = require('tape');

var rectangle1 = new rectangle.Rectangle(4, 5);

tape(function(t) {
  t.deepEqual(rectangle1.getArea(), 20);
  t.deepEqual(rectangle1.getCircumference(), 18);
  t.end();
});
