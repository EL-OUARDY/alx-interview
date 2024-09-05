#!/usr/bin/node

// Import the request module to make HTTP requests
const request = require("request");

// The first command-line argument passed is the Movie ID (e.g., 3 for "Return of the Jedi")
const movieId = process.argv[2];

// URL for the Star Wars API with the movie ID
const url = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API to get movie details
request(url, (error, response, body) => {
  if (error) {
    // Log the error if the request fails
    console.error(error);
  } else {
    // Parse the response body as JSON to get movie data
    const filmData = JSON.parse(body);

    // Extract the list of character URLs from the movie data
    const characters = filmData.characters;

    // Loop through each character URL in the list
    characters.forEach((characterUrl) => {
      // Make a request to the character URL to get the character details
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          // Log the error if the request fails
          console.error(charError);
        } else {
          // Parse the response body as JSON to get character data
          const characterData = JSON.parse(charBody);

          // Print the character's name to the console
          console.log(characterData.name);
        }
      });
    });
  }
});
