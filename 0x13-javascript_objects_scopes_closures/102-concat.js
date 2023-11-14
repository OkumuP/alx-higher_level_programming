#!/usr/bin/node
const fs = require('fs');

function concatFiles(sourceFilePath1, sourceFilePath2, destinationFilePath) {
  try {
    const data1 = fs.readFileSync(sourceFilePath1, 'utf8');
    const data2 = fs.readFileSync(sourceFilePath2, 'utf8');

    const concatenatedData = data1 + data2;

    fs.writeFileSync(destinationFilePath, concatenatedData, 'utf8');

    console.log('Files concatenated successfully.');
  } catch (error) {
    console.error('Error concatenating files:', error.message);
  }
};
