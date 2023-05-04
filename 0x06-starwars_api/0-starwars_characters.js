#!/usr/bin/node

const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api';

const argument = process.argv[2];

request({ url: `${BASE_URL}/films/${argument}`, json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = response.body.characters;
    const promises = characters.map(character => {
      return new Promise(resolve => {
        request({ url: character, json: true }, function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            resolve(body.name);
          }
        });
      });
    });
    Promise.all(promises)
      .then(names => {
        console.log(names.join('\n'));
      })
      .catch(error => {
        console.log(error);
      });
  }
});
