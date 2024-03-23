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

{% extends 'base.html' %}
{% load static %}
{% block title %} Test form Us {% endblock %}
{% block content %}
<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
<div class="container">
    <h2>Book Selection Form</h2>
    <form id="borrowBookForm">
        <div class="form-row">
            <div class="col">
                <div class="form-group">
                    <label for="selectBooks">Select Books (Multi-Select):</label>
                    <select id="selectBooks" class="form-control" multiple></select>
                </div>
            </div>
            <div class="col">
                <div class="form-group" id="authorContainer">
                    <label for="selectAuthor">Author:</label>
                    <select id="selectAuthor" class="form-control" multiple></select>
                </div>
            </div>
        </div>
        <div class="form-group">
            <label for="selectUser">Select User:</label>
            <select id="selectUser" class="form-control"></select>
        </div>
    </form>
    <div class="form-group">
        <button type="button" class="btn btn-secondary">Submit</button>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js" defer></script>
<script>
    $(document).ready(function() {
        // Initialize select2 for the author field
        $('#selectAuthor').select2({
            placeholder: 'Select author',
            multiple: true, // Enable multi-select
            tags: true // Allow custom tags
        });

        $('#selectBooks').select2({
            placeholder: 'Select books',
            ajax: {
                url: "{% url 'get_books' %}",
                dataType: 'json',
                processResults: function(data) {
                    return {
                        results: data.results
                    };
                }
            }
        });

        $('#selectBooks').on('change', function() {
            var selectedBookIds = $(this).val(); // Get the selected book IDs
            if (selectedBookIds) {
                $.ajax({
                    url: "{% url 'get_authors_for_books' %}",
                    method: 'GET',
                    data: { book_ids: selectedBookIds },
                    success: function(response) {
                        $('#selectAuthor').empty(); // Clear the author dropdown
                        $('#selectAuthor').select2({
                            placeholder: 'Select author',
                            data: response.results
                        });
                    },
                    error: function(xhr, status, error) {
                        console.error('Error fetching authors for books:', error);
                    }
                });
            }
        });

        $('#selectUser').select2({
            placeholder: 'Select user',
            ajax: {
                url: "{% url 'get_users' %}",
                dataType: 'json',
                processResults: function(data) {
                    return {
                        results: data.results
                    };
                }
            }
        });
    });
</script>
{% endblock %}
