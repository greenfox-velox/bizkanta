// replace the list items' content with items from this list:
// ['apple', 'banana', 'cat', 'dog']

listItems = document.querySelectorAll('li');
newList = ['apple', 'banana', 'cat', 'dog'];

// newList.forEach(function(e, i) {});
//
// for (var i = 0; i < listItems.length; i++) {
//   listItems[i].innerHTML = newList[i];
// }

listItems.forEach(function(e, i) {e.innerHTML = newList[i]});
