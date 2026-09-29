#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const todos = JSON.parse(body);
  const result = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      result[todo.userId] = (result[todo.userId] || 0) + 1;
    }
  });

  console.log(result);
});
