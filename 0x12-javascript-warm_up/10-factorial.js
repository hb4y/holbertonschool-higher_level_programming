#!/usr/bin/node

const process = require('process');

const args = process.argv;
const number = parseInt(args[2]);

function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

if (number) {
  console.log(factorial(number));
} else {
  console.log(1);
}
