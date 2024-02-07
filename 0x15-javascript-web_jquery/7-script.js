// Wait for the document to be ready
$(document).ready(function () {
  // Fetch the character data from the URL
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Extract the character name from the fetched data
    const characterName = data.name;
    // Display the character name in the DIV#character
    $('DIV#character').text(characterName);
  });
});
