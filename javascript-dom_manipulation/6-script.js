// Use the Fetch API to retrieve the character data
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Extract the character name from the data
    const characterName = data.name;
    
    // Display the character name in the HTML tag with ID 'character'
    document.getElementById('character').innerText = characterName;
  })
  .catch(error => console.error('Error:', error)); // Log any errors
