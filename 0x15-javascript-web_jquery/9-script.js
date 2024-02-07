$(document).ready(function () {
  // Fetch the translation data from the URL
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Extract the translation of "hello"
    const helloTranslation = data.hello;
    // Display the translation in the DIV#hello
    $('DIV#hello').text(helloTranslation);
  });
});
