var actualIndex = 3;

var images = [
  'pictures/img_1.jpg',
  'pictures/img_2.jpg',
  'pictures/img_3.jpg',
  'pictures/img_4.jpg',
  'pictures/img_5.jpg',
  'pictures/img_6.jpg',
];

var thumbnails = document.querySelector('.thumbnails');
var prevButton = document.querySelector('.arrow_left');
var nextButton = document.querySelector('.arrow_right');
var thumbnailsPrevButton = document.querySelector('.littlepic_arrow_left');
var thumbnailsNextButton = document.querySelector('.littlepic_arrow_right');
var mainpic = document.querySelector('.mainpic');
var imgTitle = document.querySelector('h4');

updateState();

thumbnails.addEventListener('click', changeImgByClicking);
prevButton.addEventListener('click', prevWithArrow);
nextButton.addEventListener('click', nextWithArrow);
thumbnailsPrevButton.addEventListener('click', prevWithArrow);
thumbnailsNextButton.addEventListener('click', nextWithArrow);

function updateState() {
  generateThumbnails();
  setMainImgSrc();
  setImgTitle();
}

function setMainImgSrc() {
  mainpic.setAttribute('src', images[actualIndex])
}

function setImgTitle() {
  imgTitle.textContent = images[actualIndex];
}

function generateThumbnails() {
  thumbnails.innerHTML = '';
  var visibleThumbnails = getVisibleThumbnails();
  visibleThumbnails.forEach(function(src) {
    var thumbnail = document.createElement('img');
    var index = images.indexOf(src);
    thumbnail.setAttribute('src', src);
    thumbnail.setAttribute('data-index', index);
    thumbnail.classList.add('pic');
    thumbnails.appendChild(thumbnail);
  });
}

function getVisibleThumbnails() {
  var prev = images[getIndexByStep(-1)];
  var current = images[actualIndex];
  var next = images[getIndexByStep(1)];
  return [prev, current, next];
}

function nextWithArrow() {
  changeImgByStep(1);
}

function prevWithArrow() {
  changeImgByStep(-1);
}

function changeImgByStep(step) {
  actualIndex = getIndexByStep(step);
  updateState();
}

function getIndexByStep(step) {
  return (actualIndex + step + images.length) % images.length;
}

function changeImgByClicking(event) {
  var element = event.target;
  if (element.src) {
    actualIndex = parseInt(element.getAttribute('data-index'));
    updateState();
  }
}
