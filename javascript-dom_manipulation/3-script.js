// Get the header element
const toggleHeaderDiv = document.querySelector('header');

// Get the toggle_header element
const toggleHeaderElement = document.getElementById('toggle_header');

// Add a click event listener to the toggle_header element
toggleHeaderElement.addEventListener('click', () => {
  // Toggle the class between red and green
  if (toggleHeaderDiv.classList.contains('red')) {
    toggleHeaderDiv.classList.remove('red');
    toggleHeaderDiv.classList.add('green');
  } else {
    toggleHeaderDiv.classList.remove('green');
    toggleHeaderDiv.classList.add('red');
  }
});
