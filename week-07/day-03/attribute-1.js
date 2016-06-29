 // Write the image's url to the console.
var greenFox = document.querySelector('img');
console.log(greenFox.getAttribute('src'));
// Replace the image with a picture of yourself.
greenFox.setAttribute('src', 'http://sailormoonrpg.com/wp-content/uploads/2016/01/sailor-moon-sailor-moon-quiz.jpg');
// Make the link point to the Green Fox Academy website.
var link = document.querySelector('a');
link.setAttribute('href', 'http://www.greenfoxacademy.com/')
// Disable the second button.
var secondButton = document.querySelector('.this-one')
secondButton.disabled = true;
// Replace its text with 'Don't click me!'.
secondButton.textContent = "Don't click me!"
