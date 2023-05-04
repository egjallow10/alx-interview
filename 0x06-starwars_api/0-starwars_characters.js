#!/usr/bin/node

const requests = require('request');
const { json } = require('stream/consumers');
const BASE_URL = `https://swapi-api.alx-tools.com/api`
const argument = process.argv[2]

requests({url:`${BASE_URL}/films/3`, json:true}, async function (error, response, body) {
    if(error){
        console.log(error)
    }
    const { characters } = await response.body;
    //    console.log(characters)
       characters.forEach(element => {
            new Promise( (resolve,reject)=>{
            requests({uri:element,json:true}, async function(error, response){
                // const {name} = await response.body
                console.log(await response.body.name)
            })
            })
       });

 });