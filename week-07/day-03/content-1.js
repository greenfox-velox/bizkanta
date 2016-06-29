// 1. Alert the content of the heading.
var h1 = document.querySelector('h1');
alert(h1.textContent);
// 2. Write the content of the first paragraph to the console.
var firstP = document.querySelector('p');
console.log(firstP.textContent);
// 3. Alert the content of the second paragraph.
var secondP = document.querySelector('.other');
alert(secondP.textContent);
// 4. Replace the heading's content with 'New content'.
h1.innerHTML = 'New content';
// 5. Replace the last paragraph's content with the first paragraph's content.
var lastP = document.querySelector('.result');
lastP.innerHTML = firstP.innerHTML;
