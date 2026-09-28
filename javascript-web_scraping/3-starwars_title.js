#!/usr/bin/node

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const film = JSON.parse(body);
  console.log(film.title);
});
