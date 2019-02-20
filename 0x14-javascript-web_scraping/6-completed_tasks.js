#!/usr/bin/node

const request = require('request');

let endpoint = process.argv[2];
const dict = {};
request(endpoint, function (error, response, body) {
  if (!error) {
    for (let task of JSON.parse(body)) {
      if (task.completed) {
        if (dict[task.userId.toString()]) {
          dict[task.userId.toString()]++;
        } else {
          dict[task.userId.toString()] = 1;
        }
      }
    }
    console.log(dict);
  }
});
