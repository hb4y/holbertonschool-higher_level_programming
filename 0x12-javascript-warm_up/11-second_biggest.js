#!/usr/bin/node

const process = require('process');

const args = process.argv;
const len = args.length;
let first = -Infinity;
let second = -Infinity;
let number;

if (len <= 2) {
  console.log(0);
} else if (len === 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    number = parseInt(args[i]);
    if (number > first) {
      second = first;
      first = number;
    } else if (number > second) {
      second = number;
    }
  }
  console.log(second);
}
