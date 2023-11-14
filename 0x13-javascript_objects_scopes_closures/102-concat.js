#!/usr/bin/node
const fs = require('fs');

function concatFiles(sourceFilePath1, sourceFilePath2, destinationFilePath) {
  try {
    // Read the contents of the first file
    const data1 = fs.readFileSync(sourceFilePath1, 'utf8');

    // Read the contents of the second file
    const data2 = fs.readFileSync(sourceFilePath2, 'utf8');

    // Concatenate the contents of the two files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFileSync(destinationFilePath, concatenatedData, 'utf8');

    console.log('Files concatenated successfully.');
  } catch (error) {
    console.error('Error concatenating files:', error.message);
  }
};
