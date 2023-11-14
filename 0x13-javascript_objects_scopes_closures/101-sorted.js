#!/usr/bin/node
const originalData = require('./101-data').dict;

const entries = Object.entries(originalData);
const values = Object.values(originalData);
const uniqueValues = [...new Set(values)];
const resultDictionary = {};

for (const uniqueValue of uniqueValues) {
  const matchingKeys = [];
  for (const entry of entries) {
    if (entry[1] === uniqueValue) {
      matchingKeys.unshift(entry[0]);
    }
  }
  resultDictionary[uniqueValue] = matchingKeys;
}

console.log(resultDictionary);
