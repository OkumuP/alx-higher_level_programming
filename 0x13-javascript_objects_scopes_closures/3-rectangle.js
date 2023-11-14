#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let v = '';
      for (let b = 0; b < this.width; b++) {
        v += 'X';
      }
      console.log(v);
    }
  }
}
module.exports = Rectangle;
