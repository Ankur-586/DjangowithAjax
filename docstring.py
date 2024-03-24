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

$(document).ready(function() {
    // Initialize select2 after the modal is shown
    $('#borrowModal').on('shown.bs.modal', function () {
        // Initialize select2 for the author field
        $('#selectAuthor').select2({
            placeholder: 'Select author',
            multiple: true,
            tags: true
        });

        $('#selectBooks').select2({
            placeholder: 'Select books',
            ajax: {
                url: get_books,
                dataType: 'json',
                processResults: function(data) {
                    return { results: data.results };
                }
            }
        });

        $('#selectBooks').on('change', function() {
            var selectedBookIds = $(this).val();
            if (selectedBookIds) {
                $.ajax({
                    url: get_authors_for_books,
                    method: 'GET',
                    data: { book_ids: selectedBookIds },
                    success: function(response) {
                        var selectedAuthors = $('#selectAuthor').val();
                        $('#selectAuthor').empty().select2({
                            placeholder: 'Select author',
                            data: response.results
                        }).val(selectedAuthors).trigger('change');
                    },
                    error: function(xhr, status, error) {
                        console.error('Error fetching authors for books:', error);
                    }
                });
            }
        });

        $('#selectBranch').select2({
            placeholder: 'Select Branch',
            ajax: {
                url: get_branch,
                dataType: 'json',
                processResults: function(data) {
                    return { results: data.results };
                }
            }
        });

        $('#selectUser').prop('disabled', true);
        $('#selectBranch').on('change', function() {
            var selectedBranch = $(this).val();
            if (selectedBranch) {
                $('#selectUser').prop('disabled', false);
                $.ajax({
                    url: get_users_by_branch,
                    method: 'GET',
                    data: { branch: selectedBranch },
                    dataType: 'json',
                    success: function(response) {
                        $('#selectUser').empty();
                        if (response.results.length > 0) {
                            response.results.forEach(function(user) {
                                $('#selectUser').append($('<option>', {
                                    value: user.id,
                                    text: user.email
                                }));
                            });
                        } else {
                            $('#selectUser').append($('<option>', {
                                value: '',
                                text: 'No users found'
                            }));
                        }
                    },
                    error: function(xhr, status, error) {
                        console.error('Error fetching users for branch:', error);
                    }
                });
            } else {
                $('#selectUser').prop('disabled', true);
                $('#selectUser').empty();
            }
        });
    });
    
    // Submit form when save button is clicked
    $('#saveChangesBtn').on('click', function() {
        $('#borrowBookForm').submit();
    });

    $('#borrowBookForm').on('submit', function(event) {
        event.preventDefault();
        var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        var formData = {
            books: $('#selectBooks').val(),
            book_borrower_student: $('#selectUser').val(),
            branch: $('#selectBranch').val(),
        };
    
        $.ajax({
            url: save_borrower,
            method: 'POST',
            headers: { "X-CSRFToken": csrftoken },
            data: formData,
            dataType: 'json',
            success: function(response) {
                console.log('Form submitted successfully:', response);
                $('#successMessage').text(response.message).show().delay(2000).fadeOut('slow');
                $('#borrowModal').modal('hide');
                updateTable();
            },
            error: function(xhr, status, error) {
                // console.error('Error submitting form:', error);
                // Display the error message on the page
                $('#errorMessage').text('Error submitting form: ' + error).show();
            },
        });
    });
});
// Function to update the table content
function updateTable() {
    // Send an AJAX request to fetch updated data for the table
    $.ajax({
        url: get_updated_data_for_table,
        method: 'GET',
        dataType: 'json',  // Specify that we expect JSON data in the response
        success: function(response) {
            // Clear the existing table rows
            $('#tab4 tbody').empty();

            // Append the updated data to the table
            response.forEach(function(borrow) {
                var row = $('<tr>');
                row.append($('<td>').text(borrow.id));
                row.append($('<td>').text(borrow.book_name));
                row.append($('<td>').text(borrow.author_name));
                row.append($('<td>').text(borrow.book_borrower_student));
                row.append($('<td>').text(borrow.student_name));
                row.append($('<td>').text(borrow.branch));
                row.append($('<td>').text(borrow.borrow_date));
                row.append($('<td>').text(borrow.due_date));
                var returnDate = borrow.return_date ? borrow.return_date : 'None';
                row.append($('<td>').text(returnDate));
                
                var returnButton = $('<button>', {
                    'type': 'button',
                    'class': 'btn btn-secondary',
                    'data-bs-toggle': 'modal',
                    'data-bs-target': '#returnModal',
                    'data-student-id': borrow.book_borrower_student_user_id,
                    'data-return-date': borrow.return_date,
                    'data-borrow-id': borrow.id,
                    'text': 'Return Book'
                });
                var returnCell = $('<td>').append(returnButton);
                row.append(returnCell);

                // Add Delete button
                var deleteButton = $('<button>', {
                    'type': 'button',
                    'class': 'btn btn-secondary delete-btn',
                    'data-borrower-id': borrow.id,
                    'text': 'Delete'
                });
                var deleteCell = $('<td>').append(deleteButton);
                row.append(deleteCell);
                // Add other table cells as needed
                $('#tab4 tbody').append(row);
            });
        },
        error: function(xhr, status, error) {
            console.error('Error fetching updated table data:', error);
        }
    });
}

