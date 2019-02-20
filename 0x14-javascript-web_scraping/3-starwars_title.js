#!/usr/bin/node

const request = require('request');

let endpoint = 'http://swapi.co/api/films/' + process.argv[2];
request(endpoint, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
