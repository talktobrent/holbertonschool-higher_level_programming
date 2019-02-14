#!/usr/bin/node
function fact (x) {
  if (x !== 0 && !isNaN(x)) {
    return (x * fact(x - 1));
  } else {
    return (1);
  }
}
console.log(fact(parseInt(process.argv[2])).toString());
