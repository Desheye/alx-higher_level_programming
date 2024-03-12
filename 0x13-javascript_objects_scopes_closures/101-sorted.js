#!/usr/bin/node
const inputDict = require('./101-data').dict;

const entries = Object.entries(inputDict);
const values = Object.values(inputDict);
const uniqueValues = [...new Set(values)];
const outputDict = {};

for (const value of uniqueValues) {
  const keysList = [];
  for (const [key, val] of entries) {
    if (val === value) {
      keysList.unshift(key);
    }
  }
  outputDict[value] = keysList;
}

console.log(outputDict);
