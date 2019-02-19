#!/usr/bin/node

const dict = require('./101-data.js').dict;

let newdict = {};

for (let x in dict) {
  if (dict[x].toString() in newdict) {
    continue;
  }
  for (let y in dict) {
    if (dict[y] === dict[x]) {
      if (newdict[dict[x].toString()]) {
        newdict[dict[x].toString()].push(y);
      } else {
        newdict[dict[x].toString()] = [y];
      }
    }
  }
}
console.log(newdict);
