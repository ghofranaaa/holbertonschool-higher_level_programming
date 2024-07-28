// Use the Fetch API to retrieve the greeting
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Select the div element with the ID 'hello'
    const greetingElement = document.getElementById('hello');
    
    // Display the greeting in the HTML element
    greetingElement.innerText = data.hello;
  })
  .catch(error => console.error('Error:', error)); // Log any errors
