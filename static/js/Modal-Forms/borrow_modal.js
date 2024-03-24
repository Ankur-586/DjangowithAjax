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
