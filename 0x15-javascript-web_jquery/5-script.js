// Wait for the document to be ready
$(document).ready(function () {
  // Add a click event listener to the DIV#add_item
  $('DIV#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>Item</li>');
    // Append the new <li> element to the UL.my_list
    $('ul.my_list').append(newItem);
  });
});
