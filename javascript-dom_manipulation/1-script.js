const redHeaderDiv = document.getElementById('red_header');

redHeaderDiv.addEventListener('click', function() {
  const headerElement = document.querySelector('header');
  
  headerElement.style.color = '#FF0000';
});
