#!/usr/bin/node

const Sq1 = require('./5-square');

module.exports = class Square extends Sq1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      console.log(c.repeat(this.width).concat('\n').repeat(this.height).slice(0, -1));
    }
  }
};
