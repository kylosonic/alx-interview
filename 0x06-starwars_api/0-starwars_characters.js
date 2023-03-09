#!/usr/bin/node
const request = require('request');
/**
 *  @param argv
 *  @returns string
 */

let arg = process.argv.slice(2);
let url = 'https://swapi-api.alx-tools.com/api/films/'+ arg[0];
request.get(url, function (err, req, body) {
    let data  = JSON.parse(body)
    data.characters.forEach(character => {
        let people = [] // incase of the list 
        request(character, function (err, req, person) {
            let person_data = JSON.parse(person)
            console.log(person_data.name)
        })
    });
})
