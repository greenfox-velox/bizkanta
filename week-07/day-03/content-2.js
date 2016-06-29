// fill every paragraph with the last one's content.
var allParagraph = document.querySelectorAll('p');
var lastParagraph = document.querySelector('.dog');
allParagraph.forEach(function(e) {e.textContent = lastParagraph.textContent});
