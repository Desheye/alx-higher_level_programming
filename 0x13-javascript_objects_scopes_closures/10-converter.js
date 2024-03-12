#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (n) {
    const digits = '0123456789ABCDEF';
    if (n === 0) return '';
    return convertToBase(Math.floor(n / base)) + digits[n % base];
  };
};
