// Select the div element with the ID 'add_item'
const addItemDiv = document.getElementById('add_item');

// Add the click event listener to the div
addItemDiv.addEventListener('click', function() {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  
  // Select the ul element with the class 'my_list'
  const myList = document.querySelector('.my_list');
  
  // Append the new li element to the ul
  myList.appendChild(newItem);
});
