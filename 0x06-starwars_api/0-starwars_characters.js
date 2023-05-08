#!/usr/bin/node

const requests = require('request')
const BASE_URL = 'https://swapi-api.alx-tools.com/api'
const argument = process.argv[2]

requests({ url: `${BASE_URL}/films/${argument}`, json: true }, async function (error, response, body) {
  if (error) {
    console.log(error)
  }
  const characters = body.characters
  for (let index = 0; index < characters.length; index++) {
    const name = await toGetName(characters[index])
    console.log(name)
  }
})

function toGetName (url) {
  const name = new Promise((resolve, reject) => {
    requests({ url }, (error, response, body) => {
      if (error) {
        console.log(error)
      }
      resolve(JSON.parse(body).name)
    })
  })
  return name
}

