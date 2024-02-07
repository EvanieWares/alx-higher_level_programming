$(document).ready(function () {
  // Add event listener for fetching translation
  $('INPUT#btn_translate').click(function () {
    // Get the language code entered by the user
    const languageCode = $('INPUT#language_code').val();

    // Make the API request to fetch translation
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      // Display the translation in the DIV#hello
      $('DIV#hello').text(data.hello);
    });
  });
});
