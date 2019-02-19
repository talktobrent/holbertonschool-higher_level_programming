#!/usr/bin/node

let fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  console.log(err || data);
});
