#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);

  if (!filmData.characters || filmData.characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  filmData.characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.log('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.log(`Failed to retrieve character data. Status code: ${response.statusCode}`);
        return;
      }

      const characterData = JSON.parse(body);

      console.log(characterData.name);
    });
  });
});
