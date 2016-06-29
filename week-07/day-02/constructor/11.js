'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods
function Stack() {
  this.elementList = [];
  this.num_of_elements = 0;

  this.size = function() {
    return this.elementList.length;
  };

  this.push = function(element) {
    this.elementList[this.num_of_elements] = element;
    this.num_of_elements++;
  };

  this.pop = function() {
    var lastItem = this.elementList.splice(this.elementList.length - 1, 1);
    return lastItem;
  };

  this.print = function() {
    console.log(this.elementList);
  };
}

var stack = new Stack();
console.log(stack.size());
stack.push(5);
stack.push(3);
stack.push(4);
console.log(stack.pop());
console.log(stack.size());
stack.print();
