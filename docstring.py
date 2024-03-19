'''
xhr: This is the XMLHttpRequest object, which contains the response data from the server.

status: This is the status of the request (e.g., 'error', 'timeout', 'abort', etc.).

error: This is the textual portion of the HTTP status code (e.g., 'Not Found', 'Internal Server Error', etc.).

Inside the error function:

xhr.responseJSON: This retrieves the response JSON data sent by the server. In this case, it's expecting JSON data containing errors.

errors: This variable holds the error data extracted from the JSON response. It should be structured as a dictionary where keys 
represent form fields and values are lists of error messages for each field.

$.each(errors, function(field, messages) { ... }): This jQuery function iterates over each key-value pair in the errors dictionary. 
For each pair, the field variable represents the form field name, and the messages variable holds a list of error messages for that field.

$('#' + field + '_errors').text(messages.join(' '));: Inside the loop, this line selects the element with an ID corresponding 
to the form field error message container (e.g., #first_name_errors, #email_errors, etc.). It then sets the text content of this 
element to the error messages joined into a single string. The join(' ') method joins the messages in the messages list with a space between them.

So, essentially, this code iterates over the error messages received from the server and updates the corresponding error message 
containers in the HTML form with the appropriate error messages for each field.
'''

import requests

url = requests.get('https://vaaradhi.agrani.tech/api/v1/onboarding/farmers/4a373885-ed6e-4a0d-b77d-346b19ae5929')

''' Do not delete
$(document).ready(function() {
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    var studentId;
    var returnDate;
    
    $('#returnModal').on('show.bs.modal', function(event) {
      var button = $(event.relatedTarget);
      var studentId = button.data('student-id');
      var returnDate = button.data('return-date');
      console.log(studentId, returnDate);

      // Fetch CSRF token
      var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
      // Fetch late fine information
      $.ajax({
        url: "{% url 'fine' 0 %}".replace('0', studentId),
        method: 'GET',
        headers: { "X-CSRFToken": csrftoken },
        success: function(response) {
          console.log('get ajax', response)
          if (response && response.late_penalty !== undefined) {
            $('#lateFineContent').html('Total Fine: ' + response.late_penalty);
          } else {
            $('#lateFineContent').html('Total Fine: ' + response.late_penalty);
          }
        },
        error: function(xhr, status, error) {
          console.error(error);
          $('#lateFineContent').html('Total Fine: Error');
        }
      });

    // Handle form submission
    $('#return_date').click(function(event) {
      // Retrieve the return date from the input field
      var returnDate = $('#returnDate').val();
      console.log(returnDate); // Check if the value is retrieved correctly
      //var studentId = $(this).data('data-student-id');
      //console.log('tr',studentId)
      // Close the modal
      //$('#returnModal').modal('hide');

      // Send AJAX request to the Django view
      $.ajax({
          url: "{% url 'fine' 0 %}".replace('0', studentId),
          type: 'POST',
          headers: { "X-CSRFToken": csrftoken },
          data: {
              'returnDate': returnDate // Include returnDate in the data
          },
          success: function(response) {
              // Display success message
              $('#successMessage').text(response.message);
              $('#successMessage').show().delay(2000).fadeOut('slow');
          },
          error: function(xhr, status, error) {
              // Display error message
              console.error("Error:", error);
              $('#successMessage').text("An error occurred while processing the request");
              $('#successMessage').show().delay(2000).fadeOut('slow');
          }
      });
    });
  });
  });
  '''