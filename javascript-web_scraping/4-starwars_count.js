#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const films = JSON.parse(body).results;
  const count = films.filter(
    (film) => film.characters.some((url) => /\/18\/?$/.test(url))
  ).length;

  console.log(count);
});
