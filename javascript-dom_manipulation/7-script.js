// Use the Fetch API to retrieve the list of movies
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Select the ul element with the ID 'list_movies'
    const movieList = document.getElementById('list_movies');
    
    // Iterate over each movie in the data array
    data.results.forEach(movie => {
      // Create a new li element for each movie
      const listItem = document.createElement('li');
      
      // Set the text content of the li element to the movie title
      listItem.textContent = movie.title;
      
      // Append the li element to the ul
      movieList.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error:', error)); // Log any errors
