var dog = (function(){
  var sound = 'woof';

  return {
    talk: function(){
      console.log(sound);
    }
  };
})();

var tacsi = dog();
tacsi.talk();
