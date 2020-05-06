#!/usr/bin/node

exports.add = function (a, b) {
  const first = parseInt(a);
  const second = parseInt(b);

  if (first && second) {
    return (first + second);
  } else {
    return (NaN);
  }
};
