var dog = (function(){
  var sound = 'woof';

  function talk(){
    console.log(sound);
  }

  return {
    talk: talk
  };
})();

dog.talk();
