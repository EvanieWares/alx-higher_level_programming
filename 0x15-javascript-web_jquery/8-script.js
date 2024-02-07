// Wait for the document to be ready
$(document).ready(function () {
  // Fetch the movies data from the URL
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Iterate through each movie in the fetched data
    $.each(data.results, function (index, movie) {
      // Extract the movie title
      const title = movie.title;
      // Create a new list item with the movie title
      const listItem = $('<li>').text(title);
      // Append the new list item to the UL#list_movies
      $('UL#list_movies').append(listItem);
    });
  });
});
