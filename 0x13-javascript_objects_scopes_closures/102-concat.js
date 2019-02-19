#!/usr/bin/node

let fs = require('fs');

let buffer = fs.readFileSync(process.argv[2], { encoding: 'utf-8', flag: 'r' });
let buffer2 = fs.readFileSync(process.argv[3], { encoding: 'utf-8', flag: 'r' });
fs.writeFileSync(process.argv[4], buffer.concat(buffer2));
