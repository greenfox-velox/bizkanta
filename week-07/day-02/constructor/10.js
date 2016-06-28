'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

function Student() {
  this.gradeList = [];
  this.addgrade = function(grade) {
    this.gradeList.push(grade);
    return this.gradeList;
  };

  this.getAverage = function() {
    var averageGrade = 0;
    this.gradeList.forEach(function(e) {
      averageGrade += e;
    });
    return averageGrade / this.gradeList.length;
  };
}

var student = new Student();
student.addgrade(2);
student.addgrade(5);
student.addgrade(4);
// console.log(student.gradeList);
console.log(student.getAverage());
