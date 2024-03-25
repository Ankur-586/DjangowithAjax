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

# $(document).ready(function() {
#     // Initialize select2 after the modal is shown
#     $('#borrowModal').on('shown.bs.modal', function () {
#         // Initialize select2 for the author field
#         $('#selectAuthor').select2({
#             placeholder: 'Select author',
#             multiple: true,
#             tags: true
#         });

#         $('#selectBooks').select2({
#             placeholder: 'Select books',
#             ajax: {
#                 url: get_books,
#                 dataType: 'json',
#                 processResults: function(data) {
#                     return { results: data.results };
#                 }
#             }
#         });

#         $('#selectBooks').on('change', function() {
#             var selectedBookIds = $(this).val();
#             if (selectedBookIds) {
#                 $.ajax({
#                     url: get_authors_for_books,
#                     method: 'GET',
#                     data: { book_ids: selectedBookIds },
#                     success: function(response) {
#                         var selectedAuthors = $('#selectAuthor').val();
#                         $('#selectAuthor').empty().select2({
#                             placeholder: 'Select author',
#                             data: response.results
#                         }).val(selectedAuthors).trigger('change');
#                     },
#                     error: function(xhr, status, error) {
#                         console.error('Error fetching authors for books:', error);
#                     }
#                 });
#             }
#         });

#         $('#selectBranch').select2({
#             placeholder: 'Select Branch',
#             ajax: {
#                 url: get_branch,
#                 dataType: 'json',
#                 processResults: function(data) {
#                     return { results: data.results };
#                 }
#             }
#         });

#         $('#selectUser').prop('disabled', true);
#         $('#selectBranch').on('change', function() {
#             var selectedBranch = $(this).val();
#             if (selectedBranch) {
#                 $('#selectUser').prop('disabled', false);
#                 $.ajax({
#                     url: get_users_by_branch,
#                     method: 'GET',
#                     data: { branch: selectedBranch },
#                     dataType: 'json',
#                     success: function(response) {
#                         $('#selectUser').empty();
#                         if (response.results.length > 0) {
#                             response.results.forEach(function(user) {
#                                 $('#selectUser').append($('<option>', {
#                                     value: user.id,
#                                     text: user.email
#                                 }));
#                             });
#                         } else {
#                             $('#selectUser').append($('<option>', {
#                                 value: '',
#                                 text: 'No users found'
#                             }));
#                         }
#                     },
#                     error: function(xhr, status, error) {
#                         console.error('Error fetching users for branch:', error);
#                     }
#                 });
#             } else {
#                 $('#selectUser').prop('disabled', true);
#                 $('#selectUser').empty();
#             }
#         });
#     });
    
#     // Submit form when save button is clicked
#     $('#saveChangesBtn').on('click', function() {
#         $('#borrowBookForm').submit();
#     });

#     $('#borrowBookForm').on('submit', function(event) {
#         event.preventDefault();
#         var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
#         var formData = {
#             books: $('#selectBooks').val(),
#             book_borrower_student: $('#selectUser').val(),
#             branch: $('#selectBranch').val(),
#         };
    
#         $.ajax({
#             url: save_borrower,
#             method: 'POST',
#             headers: { "X-CSRFToken": csrftoken },
#             data: formData,
#             dataType: 'json',
#             success: function(response) {
#                 console.log('Form submitted successfully:', response);
#                 $('#successMessage').text(response.message).show().delay(2000).fadeOut('slow');
#                 $('#borrowModal').modal('hide');
#                 updateTable();
#             },
#             error: function(xhr, status, error) {
#                 // console.error('Error submitting form:', error);
#                 // Display the error message on the page
#                 $('#errorMessage').text('Error submitting form: ' + error).show();
#             },
#         });
#     });
# });
# // Function to update the table content
# function updateTable() {
#     // Send an AJAX request to fetch updated data for the table
#     $.ajax({
#         url: get_updated_data_for_table,
#         method: 'GET',
#         dataType: 'json',  // Specify that we expect JSON data in the response
#         success: function(response) {
#             // Clear the existing table rows
#             $('#tab4 tbody').empty();

#             // Append the updated data to the table
#             response.forEach(function(borrow) {
#                 var row = $('<tr>');
#                 row.append($('<td>').text(borrow.id));
#                 row.append($('<td>').text(borrow.book_name));
#                 row.append($('<td>').text(borrow.author_name));
#                 row.append($('<td>').text(borrow.book_borrower_student));
#                 row.append($('<td>').text(borrow.student_name));
#                 row.append($('<td>').text(borrow.branch));
#                 row.append($('<td>').text(borrow.borrow_date));
#                 row.append($('<td>').text(borrow.due_date));
#                 var returnDate = borrow.return_date ? borrow.return_date : 'None';
#                 row.append($('<td>').text(returnDate));
                
#                 var returnButton = $('<button>', {
#                     'type': 'button',
#                     'class': 'btn btn-secondary',
#                     'data-bs-toggle': 'modal',
#                     'data-bs-target': '#returnModal',
#                     'data-student-id': borrow.book_borrower_student_user_id,
#                     'data-return-date': borrow.return_date,
#                     'data-borrow-id': borrow.id,
#                     'text': 'Return Book'
#                 });
#                 var returnCell = $('<td>').append(returnButton);
#                 row.append(returnCell);

#                 // Add Delete button
#                 var deleteButton = $('<button>', {
#                     'type': 'button',
#                     'class': 'btn btn-secondary delete-btn',
#                     'data-borrower-id': borrow.id,
#                     'text': 'Delete'
#                 });
#                 var deleteCell = $('<td>').append(deleteButton);
#                 row.append(deleteCell);
#                 // Add other table cells as needed
#                 $('#tab4 tbody').append(row);
#             });
#         },
#         error: function(xhr, status, error) {
#             console.error('Error fetching updated table data:', error);
#         }
#     });
# }

# dont delete
'''
<div id="tab4" class="tab-pane fade">
                <table class="table table-dark table-bordered text-center">
                    <thead>
                        <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Book Name</th>
                            <th scope="col">Author Name</th>
                            <th scope="col">Book Borrower Student</th>
                            <th scope="col">Student Name</th>
                            <th scope="col">Branch</th>
                            <th scope="col">Borrow Date</th>
                            <th scope="col">Due Date</th>
                            <th scope="col">Return Date</th>
                            <th scope="col">Return Book</th>
                            <th scope="col">Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for borrow in borrower %}
                        <tr>
                            <tr id="borrowerRow_{{ borrow.id }}">
                            <th scope="row">{{ borrow.id }}</th>
                            <td>
                                {{ borrow.books.all|join:", " }}
                            </td>
                            <td>
                                {% for book in borrow.books.all %}
                                    {{ book.author.name }}
                                    {% if not forloop.last %}, {% endif %}
                                {% endfor %}
                            </td>
                            <td>{{ borrow.book_borrower_student }}</td>
                            <th scope="row">{{ borrow.book_borrower_student.full_name }}</th>
                            <td>{{  borrow.branch }}</td>
                            <td>{{  borrow.borrow_date }}</td>
                            <td>{{ borrow.due_date }}</td>
                            <td>{{ borrow.return_date }}</td>
                            <td>
                                <button type='button' class='btn btn-secondary' data-bs-toggle="modal" data-bs-target="#returnModal" 
                                data-student-id="{{ borrow.book_borrower_student.user.id }}" data-return-date="{{ borrow.return_date }}" 
                                data-borrow-id="{{ borrow.id }}">Return Book</button>
                            </td>
                            <td><button type='button' class="btn btn-secondary delete-btn" data-borrower-id="{{ borrow.id }}">Delete</button></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                <div class="row">
                    <div class="col-sm-2">
                        <button type="button" class="btn btn-secondary" style="float:left;" data-bs-toggle="modal" data-bs-target="#borrowModal">
                            Create Borrower 
                        </button>
                    </div>
                    {% comment %} <div class="col-sm-2">
                        <a type="button" class="btn btn-secondary" href="{% url 'test' %}" target="_blank">Issue Book</a>
                    </div> {% endcomment %}
                    <div class="col-sm-8"><div id="successMessage" class="alert alert-success" role="alert" style="display:none;height:70%;"></div>
                    <div class="col-sm-10"><div id="errorMessage" class="alert alert-danger" role="alert" style="display:none;height:70%;"></div>
                </div>
            </div>
'''
'''
withdatatable
{% extends 'base.html' %}
{% load static %}
{% block content %}
    <div class="container">
        <h6 class="lib text-center mt-3" style="color:gray;">Library Management System</h2>
        <ul class="nav nav-tabs">
            <li class="nav-item">
                <a class="nav-link active text-danger" data-toggle="tab" href="#tab1">LibraryCard</a>
            </li>
            <li class="nav-item">
                <a class="nav-link text-danger" data-toggle="tab" href="#tab2">Book</a>
            </li>
            <li class="nav-item">
                <a class="nav-link text-danger" data-toggle="tab" href="#tab3">Student Information</a>
            </li>
            <li class="nav-item">
                <a class="nav-link text-danger" data-toggle="tab" href="#tab4">Borrower</a>
            </li>
        </ul>
        <div class="tab-content">
            <div id="tab1" class="tab-pane fade show active">
                <table class="table table-dark table-bordered text-center">
                    <thead>
                        <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Card Number</th>
                            <th scope="col">Issued Date</th>
                            <th scope="col">Expiration Date</th>
                            <th scope="col">User</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for card in library_card %}
                        <tr>
                            <th scope="row">{{ card.id }}</th>
                            <th scope="row">{{ card.card_number }}</th>
                            <td>{{ card.issued_date }}</td>
                            <td>{{ card.expiration_date }}</td>
                            <td>{{ card.user }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            <div id="tab2" class="tab-pane fade">
                <table class="table table-dark table-bordered text-center">
                    <thead>
                        <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Title</th>
                            <th scope="col">Author</th>
                            <th scope="col">Publication Year</th>
                            <th scope="col">Isbn</th>
                            <th scope="col">Quantity</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for bk in books %}
                        <tr>
                            <th scope="row">{{ bk.id }}</th>
                            <th scope="row">{{ bk.title }}</th>
                            <td>{{ bk.author }}</td>
                            <td>{{ bk.publication_year }}</td>
                            <td>{{ bk.isbn }}</td>
                            <td>{{ bk.quantity }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            <div id="tab3" class="tab-pane fade">
                <table class="table table-dark table-dark table-bordered text-center">
                    <thead>
                        <tr>
                            <th scope="col">Id</th>
                            <th scope="col">User</th>
                            <th scope="col">Student Id</th>
                            <th scope="col">Branch</th>
                            <th scope="col">Library Card</th>
                            <th scope="col">Penalty (in Rupees) </th>
                            <th scope="col">Address</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for bws in student_information %}
                        <tr>
                            <th scope="row">{{ bws.id }}</th>
                            <td>{{ bws.branch.user }}</td>
                            <td>{{ bws.branch.user.id }}</td>
                            <td>{{ bws.branch }}</td>
                            <td>{{ bws.library_card }}</td>
                            {% if bws.Penalty == 'No Penalty' %}
                            <td>{{ bws.Penalty }}</td>
                            {% else %}
                            <td>&#x20b9;{{ bws.Penalty }}</td>
                            {% endif %}
                            <td>{{ bws.address }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            <div id="tab4" class="tab-pane fade">
                <table id="borrower-table" class="table table-dark table-bordered text-center">
                    <thead>
                        <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Book Name</th>
                            <th scope="col">Author Name</th>
                            <th scope="col">Book Borrower Student</th>
                            <th scope="col">Student Name</th>
                            <th scope="col">Branch</th>
                            <th scope="col">Borrow Date</th>
                            <th scope="col">Due Date</th>
                            <th scope="col">Return Date</th>
                            <th scope="col">Return Book</th>
                            <th scope="col">Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for borrow in borrower %}
                        <tr>
                            <td>{{ borrow.id }}</td>
                            <td>{{ borrow.book_name }}</td>
                            <td>{{ borrow.author_name }}</td>
                            <td>{{ borrow.book_borrower_student }}</td>
                            <td>{{ borrow.student_name }}</td>
                            <td>{{ borrow.branch }}</td>
                            <td>{{ borrow.borrow_date }}</td>
                            <td>{{ borrow.due_date }}</td>
                            <td>{{ borrow.return_date }}</td>
                            <td>
                                <button type='button' class='btn btn-secondary' data-bs-toggle="modal" data-bs-target="#returnModal" 
                                data-student-id="{{ borrow.book_borrower_student_user_id }}" data-return-date="{{ borrow.return_date }}" 
                                data-borrow-id="{{ borrow.id }}">Return Book</button>
                            </td>
                            <td><button type='button' class="btn btn-secondary delete-btn" data-borrower-id="{{ borrow.id }}">Delete</button></td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                <div class="col-sm-2">
                    <button type="button" class="btn btn-secondary" style="float:left;" data-bs-toggle="modal" data-bs-target="#borrowModal">
                        Create Borrower 
                    </button>
                </div>
            </div>            
        </div>
    </div>

    <!-- Includes Bootstrap Modal -->
    {% include 'LibraryManagementSystem/borrower.html' %}
    {% include 'LibraryManagementSystem/return.html' %}
    <!-- Comment Close -->
    
{% endblock content %}

{% block scripts %}
<script>
    $(document).ready(function() {
        // Initialize DataTable for each table
        $('#tab1 table').dataTable({
            pageLength: 5
        });
        $('#tab2 table').dataTable({
            pageLength: 5
        });
        $('#tab3 table').dataTable({
            pageLength: 5
        });
        $('#tab4 table').dataTable({
            pageLength: 5 ,
            lengthMenu: [
              [5, 10, 50, -1], [5, 10, 50, 'All']
              ],
        });
    });
</script>

<script src="{% static 'js/home/table_tab.js' %}"></script> 
<script>
    var deleteBookUrl = "{% url 'delete' 0 %}";
</script>
<script src="{% static 'js/home/delete.js' %}"></script>
{% endblock %}


'''