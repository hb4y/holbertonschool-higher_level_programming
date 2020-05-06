#!/usr/bin/node

function callMeMoby (times, func) {
  for (; times > 0; times--) {
    func();
  }
}

module.exports.callMeMoby = callMeMoby;
