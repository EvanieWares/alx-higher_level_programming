// Wait for the document to be ready
$(document).ready(function () {
  // Add a click event listener to the DIV#red_header
  $('DIV#red_header').click(function () {
    // Update the text color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});
