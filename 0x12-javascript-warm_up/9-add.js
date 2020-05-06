#!/usr/bin/node

const process = require('process');

const args = process.argv;
const first = parseInt(args[2]);
const second = parseInt(args[3]);

if (first && second) {
  console.log(first + second);
} else {
  console.log(NaN);
}
