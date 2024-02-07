// Wait for the document to be ready
$(document).ready(function () {
  // Add a click event listener to the DIV#red_header
  $('DIV#red_header').click(function () {
    // Add the class 'red' to the <header> element
    $('header').addClass('red');
  });
});
