#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 1) {
      this.width = parseInt(w);
      this.height = parseInt(h);
    }
  }
  print () {
    console.log('X'.repeat(this.width).concat('\n').repeat(this.height).slice(0, -1));
  }
  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
