#!/usr/bin/node
function add (a, b) {
  console.log((a + b).toString());
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
