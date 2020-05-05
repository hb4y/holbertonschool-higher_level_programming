#!/usr/bin/node

const process = require('process');

const args = process.argv;
const number = parseInt(args[2]);

if (number) {
  for (let i = number; i > 0; i--) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
