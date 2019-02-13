#!/usr/bin/node
let last = 0;
let high = Number(process.argv[2]);
for (let x = 2; x < process.argv.length; x++) {
  if (Number(process.argv[x]) > high) {
    last = high;
    high = Number(process.argv[x]);
  }
  if (Number(process.argv[x]) > last && Number(process.argv[x]) < high) {
    last = Number(process.argv[x]);
  }
}
console.log(last.toString());
