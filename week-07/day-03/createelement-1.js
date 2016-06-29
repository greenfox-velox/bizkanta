// Add an item that says 'The Green Fox' to the asteroid list.
var asteroidList = document.querySelector('ul.asteroids');
var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroid);
// Add an item that says 'The Lamplighter' to the asteroid list.
var newAsteroid2 = document.createElement('li');
newAsteroid2.textContent = 'The Lamplighter';
asteroidList.appendChild(newAsteroid2);
// Add a heading saying 'I can add elements to the DOM!' to the .container.
var container = document.querySelector('.container')
var newh1 = document.createElement('h1');
newh1.textContent = 'I can add elements to the DOM!'
container.appendChild(newh1);
// Add an image, any image, to the container.
var newImg = document.createElement('img');
newImg.setAttribute('src', 'http://www.edenkert.hu/upload/2/article/1921/2_original.jpg')
container.appendChild(newImg);
