#!/usr/bin/node
exports.esrever = function (list) {
  let newlist = [];
  while (list.length) {
    newlist.push(list.pop());
  }
  return newlist;
};
