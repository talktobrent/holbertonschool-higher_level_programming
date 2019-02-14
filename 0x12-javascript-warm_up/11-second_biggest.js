#!/usr/bin/node
let low = 0;
let high = 0;
for (let x of process.argv.splice(2)) {
  if (Number(x) > high) {
    low = high;
    high = Number(x);
  } else if (Number(x) > low && Number(x) < high) {
    low = Number(x);
  }
}
console.log(low);
