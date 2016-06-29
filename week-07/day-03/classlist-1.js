// Does cat have a cat class?
// If so, alert 'YEAH CAT!'
var paragraphs = document.querySelectorAll('p')

paragraphs.forEach(function(e) {
  if (e.textContent === 'cat' && e.classList.contains('cat')) {
    alert('YEAH CAT!');
  }
});

// If dolphin has a 'dolphin' class, replace apple's content with 'pear'
var apple = document.querySelector('.apple');

paragraphs.forEach(function(e) {
  if (e.textContent === 'dolphin' && e.classList.contains('dolphin')) {
    apple.textContent = 'pear';
  }
});

// If apple has an 'apple' class, replace cat's content with 'dog'
var cat = document.querySelector('.cat');

paragraphs.forEach(function(e) {
  if (e.textContent === 'apple' && e.classList.contains('apple')) {
    cat.textContent = 'dog';
  }
});

// Make apple red
apple.classList.add('red');
// Make balloon less balloon-like
var baloon =  document.querySelector('.balloon');
baloon.classList.remove('balloon')
