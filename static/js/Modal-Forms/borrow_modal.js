
    // Sample data for books and authors
    // const booksData = [
    //   { id: 1, title: "Book 1", authors: ["Author 1", "Author 2"] },
    //   { id: 2, title: "Book 2", authors: ["Author 2", "Author 3"] },
    //   { id: 3, title: "Book 3", authors: ["Author 3", "Author 4"] }
    // ];

    // // Populate the select field with books
    // function populateBooksSelect() {
    //   const select = $("#bookSearch");
    //   select.empty();
    //   booksData.forEach(book => {
    //     select.append(`<option value="${book.id}">${book.title}</option>`);
    //   });
    // }

    // // Display authors of selected books
    // function displaySelectedAuthors(selectedBookIds) {
    //   const authorsList = $("#selectedAuthors");
    //   authorsList.empty();
    //   booksData.forEach(book => {
    //     if (selectedBookIds.includes(book.id)) {
    //       book.authors.forEach(author => {
    //         authorsList.append(`<li class="list-group-item">${author}</li>`);
    //       });
    //     }
    //   });
    // }

    // // Initialize the form
    // $(document).ready(function() {
    //   populateBooksSelect();

    //   $("#bookSearch").change(function() {
    //     const selectedBookIds = $(this).val() || [];
    //     displaySelectedAuthors(selectedBookIds);
    //   });

    //   // Optional: Implement form submission logic
    //   $("#bookSelectionForm").submit(function(event) {
    //     event.preventDefault();
    //     // Your form submission logic here
    //   });
    // });

<form id="borrowBookForm">
                        <div class="form-group">
                            <label for="selectBooks">Select Books (Multi-Select):</label>
                            <select id="selectBooks" class="form-control" multiple></select>
                        </div>
                        <div class="form-group">
                            <label for="selectUser">Select User:</label>
                            <select id="selectUser" class="form-control"></select>
                        </div>
                    </form>
// $(document).ready(function() {
//     $('#saveChangesBtn').click(function() {
//         var selectedBookIds = $('select[name="books"]').val();
//         var selectedStudentId = $('#student').val();
        
//         if (!selectedBookIds || selectedBookIds.length === 0) {
//             alert('Please select at least one book.');
//             return;
//         }

//         var formData = {
//             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
//             'student_pk': selectedStudentId,
//             'book_pks': selectedBookIds, // Assuming 'book_pks' is a list of book primary keys
//         };

//         $.ajax({
//             url: borrowBookUrl.replace('0', selectedStudentId),
//             type: 'POST',
//             data: formData,
//             dataType: 'json',
//             success: function(response) {
//                 $('#successMessage').delay(2000).text(response.message).show().fadeOut('slow');
//                 $('#borrowModal').modal('hide');
//             },
//             error: function(xhr, status, error) {
//                 console.error('Error saving data:', status, error);
//                 $('#errorMessage').delay(2000).text(status, error).show().fadeOut('slow');
//             }
//         });
//     });
// });

// $(document).ready(function() {
//     $('#saveChangesBtn').click(function() {
//         var selectedBookId = $('#book').val();
//         var selectedStudentId = $('#student').val();
//         var formData = {
//             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
//             'student_pk': selectedStudentId,
//             'book_pk': selectedBookId,
//         };

//         $.ajax({
//             url: borrowBookUrl.replace('0', selectedStudentId).replace('0', selectedBookId),
//             type: 'POST',
//             data: formData,
//             dataType: 'json',
//             success: function(response) {
//                 // updatePage(response.data);
//                 $('#successMessage').delay(2000).text(response.message).show().fadeOut('slow');
//                 $('#borrowModal').modal('hide');
//             },
//             error: function(xhr, status, error) {
//                 console.error('Error saving data:', status, error);
//                 $('#errorMessage').delay(2000).text(status, error).show().fadeOut('slow');
//             }
//         });
//     });

//     function updatePage(data) {
//         console.log(data)
//         // Construct the HTML for the new table row using the received data
//         var newRow = '<tr>' +
//                         '<td>' + data.id + '</td>' + // Borrower ID
//                         '<td>' + data.book.title + '</td>' + // Book Title
//                         '<td>' + data.book.id + '</td>' + // Book ID
//                         '<td>' + data.book_borrower_student.user_email + '</td>' + // Student Email
//                         '<td>' + data.book_borrower_student.id + '</td>' + // Student ID
//                         '<td>' + data.borrow_date + '</td>' + // Borrow Date
//                         '<td>' + data.due_date + '</td>' + // Due Date
//                         '<td>' + data.return_date + '</td>' + // Return Date
//                         '<td>' + data.created_at + '</td>' + // Created At
//                         '<td>' + data.updated_at + '</td>' + // Updated At
//                         '<td><button type="button" class="btn btn-secondary delete-btn" data-borrower-id="' + data.id + '">Delete</button></td>' + // Delete Button
//                      '</tr>';
    
//         // Append the new row to the table body
//         $('#tab4 tbody').append(newRow);
//     }
// });