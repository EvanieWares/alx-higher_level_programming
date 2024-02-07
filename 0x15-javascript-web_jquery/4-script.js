// Wait for the document to be ready
$(document).ready(function () {
  // Add a click event listener to the DIV#toggle_header
  $('DIV#toggle_header').click(function () {
    // Check if the <header> element has class 'red'
    if ($('header').hasClass('red')) {
      // If it has class 'red', toggle to 'green'
      $('header').removeClass('red').addClass('green');
    } else {
      // If it doesn't have class 'red', toggle to 'red'
      $('header').removeClass('green').addClass('red');
    }
  });
});
