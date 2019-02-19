#!/usr/bin/node

const dict = require('./101-data.js').dict;

let newdict = {};

for (let x in dict) {
  if (newdict[dict[x].toString()]) {
    newdict[dict[x].toString()].push(x);
  } else {
    newdict[dict[x].toString()] = [x];
  }
}
console.log(newdict);
