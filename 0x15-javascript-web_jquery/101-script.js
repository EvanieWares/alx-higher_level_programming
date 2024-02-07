$(document).ready(function () {
  // Add event listener for adding new item
  $('DIV#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>').text('Item');
    // Append the new <li> element to UL.my_list
    $('UL.my_list').append(newItem);
  });

  // Add event listener for removing last item
  $('DIV#remove_item').click(function () {
    // Remove the last <li> element from UL.my_list
    $('UL.my_list li:last-child').remove();
  });

  // Add event listener for clearing the list
  $('DIV#clear_list').click(function () {
    // Remove all <li> elements from UL.my_list
    $('UL.my_list').empty();
  });
});
