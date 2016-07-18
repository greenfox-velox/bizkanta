function Dog(sound){
  this.sound = sound;
}

Dog.prototype.talk = function(){
  console.log(this.sound);
}

var tacsi = new Dog('woof');
tacsi.talk();
