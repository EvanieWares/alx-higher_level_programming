$(document).ready(function () {
  // Add event listener for fetching translation when button is clicked
  $('INPUT#btn_translate').click(fetchTranslation);

  // Add event listener for fetching translation when ENTER is pressed in the language code input field
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  // Function to fetch translation
  function fetchTranslation () {
    // Get the language code entered by the user
    const languageCode = $('INPUT#language_code').val();

    // Make the API request to fetch translation
    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      // Display the translation in the DIV#hello
      $('DIV#hello').text(data.hello);
    });
  }
});
