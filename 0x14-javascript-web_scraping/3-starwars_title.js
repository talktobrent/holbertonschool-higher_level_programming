#!/usr/bin/node

const request = require('request');

let endpoint = 'http://swapi.co/api/films/' + process.argv[2];
request(endpoint, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
