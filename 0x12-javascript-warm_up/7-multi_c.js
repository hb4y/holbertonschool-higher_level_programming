#!/usr/bin/node

const process = require('process');

const args = process.argv;
let number = parseInt(args[2]);

if (number) {
  for (; number > 0; number--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
