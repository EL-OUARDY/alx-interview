#!/usr/bin/node

// Import the request module to make HTTP requests
const request = require('request');

// The first command-line argument passed is the Movie ID (e.g., 3 for "Return of the Jedi")
const movieId = process.argv[2];

// Check if movieId is not provided or is empty
if (!movieId) {
  console.error('Error: Movie ID must be provided as the first argument');
  process.exit(1); // Exit the script with a non-zero code to indicate an error
}

// URL for the Star Wars API with the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Helper function to make a request and return a promise
const fetchCharacter = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name); // Resolve with the character's name
      }
    });
  });
};

// Make a request to the Star Wars API to get movie details
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the response body as JSON to get movie data
    const filmData = JSON.parse(body);

    // Check if filmData is not exist
    if (filmData.detail === 'Not found') {
      console.error('Error: Movie Not Found');
      process.exit(1); // Exit the script
    }

    // Extract the list of character URLs from the movie data
    const characters = filmData.characters;

    // Map character URLs to Promises
    const characterPromises = characters.map((characterUrl) =>
      fetchCharacter(characterUrl)
    );

    // Use Promise.all to wait for all character data to be fetched
    Promise.all(characterPromises)
      .then((characterNames) => {
        // Print the character names in the correct order
        characterNames.forEach((name) => console.log(name));
      })
      .catch((error) => {
        console.error('Error fetching character data:', error);
      });
  }
});
