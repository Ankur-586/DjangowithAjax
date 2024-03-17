$(document).ready(function() {
    $('#saveChangesBtn').click(function() {
        var selectedBookId = $('#book').val();
        var selectedStudentId = $('#student').val();
        var formData = {
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'student_pk': selectedStudentId,
            'book_pk': selectedBookId,
        };

        $.ajax({
            url: borrowBookUrl.replace('0', selectedStudentId).replace('0', selectedBookId),
            type: 'POST',
            data: formData,
            dataType: 'json',
            success: function(response) {
                // updatePage(response.data);
                $('#successMessage').delay(2000).text(response.message).show().fadeOut('slow');
                $('#borrowModal').modal('hide');
            },
            error: function(xhr, status, error) {
                console.error('Error saving data:', status, error);
                $('#errorMessage').delay(2000).text(status, error).show().fadeOut('slow');
            }
        });
    });

    function updatePage(data) {
        console.log(data)
        // Construct the HTML for the new table row using the received data
        var newRow = '<tr>' +
                        '<td>' + data.id + '</td>' + // Borrower ID
                        '<td>' + data.book.title + '</td>' + // Book Title
                        '<td>' + data.book.id + '</td>' + // Book ID
                        '<td>' + data.book_borrower_student.user_email + '</td>' + // Student Email
                        '<td>' + data.book_borrower_student.id + '</td>' + // Student ID
                        '<td>' + data.borrow_date + '</td>' + // Borrow Date
                        '<td>' + data.due_date + '</td>' + // Due Date
                        '<td>' + data.return_date + '</td>' + // Return Date
                        '<td>' + data.created_at + '</td>' + // Created At
                        '<td>' + data.updated_at + '</td>' + // Updated At
                        '<td><button type="button" class="btn btn-secondary delete-btn" data-borrower-id="' + data.id + '">Delete</button></td>' + // Delete Button
                     '</tr>';
    
        // Append the new row to the table body
        $('#tab4 tbody').append(newRow);
    }
});