#!/usr/bin/node

const request = require('request');

let endpoint = 'http://swapi.co/api/films/';
request(endpoint, function (error, response, body) {
  if (!error) {
    let count = 0;
    for (let movie of JSON.parse(body).results) {
      for (let chara of movie.characters) {
        if (chara.split('/').includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
