#!/usr/bin/node

const request = require('request');
let fs = require('fs');
let endpoint = process.argv[2];

request
  .get(endpoint)
  .on('error', err => console.log(err))
  .pipe(fs.createWriteStream(process.argv[3]));
