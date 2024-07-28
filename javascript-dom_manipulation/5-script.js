// Select the div element with the ID 'update_header'
const updateHeaderDiv = document.getElementById('update_header');

// Add the click event listener to the div
updateHeaderDiv.addEventListener('click', function() {
  // Select the header element
  const headerElement = document.querySelector('header');
  
  // Update the text content of the header element
  headerElement.textContent = 'New Header!!!';
});
