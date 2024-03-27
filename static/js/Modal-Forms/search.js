$(document).ready(function() {
  $('#searchForm').on('submit', function(event) {
      event.preventDefault(); // Prevent default form submission
      var searchQuery = $('#searchInput').val();
      console.log(searchQuery);
      if (searchQuery.length > 2) { // Perform search only if query length is greater than 2
          $.ajax({
              url: search,
              type: 'GET',
              data: {
                  keyword: searchQuery
              },
              success: function(response) {
                  console.log('xyz', response); // For debugging purposes
                  // Update the content with search results
                  updateBorrowerTable(response);
              },
              error: function(xhr, status, error) {
                  console.error(error); // Handle errors during search request
                  // Display an error message to the user
              }
          });
      } else {
          // Handle case when search query is less than or equal to 2 characters
          // Optionally, you can display a message to the user
      }
  });

  function updateBorrowerTable(borrowers) {
      var tableBody = $('#tab4 table tbody');
      // Clear existing rows
      tableBody.empty();

      // Loop through the received data and add new rows to the table
      borrowers.forEach(function(borrow) {
          var row = '<tr id="borrowerRow_' + borrow.id + '">' +
              '<th scope="row">' + borrow.id + '</th>' +
              '<td>' + borrow.book_name + '</td>' +
              '<td>' + borrow.author_name + '</td>' +
              '<td>' + borrow.book_borrower_student + '</td>' +
              '<td>' + borrow.student_name + '</td>' +
              '<td>' + borrow.branch + '</td>' +
              '<td>' + borrow.borrow_date + '</td>' +
              '<td>' + borrow.due_date + '</td>' +
              '<td>' + borrow.return_date + '</td>' +
              '<td>' +
              '<button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#returnModal" ' +
              'data-student-id="' + borrow.book_borrower_student + '" data-return-date="' + borrow.return_date + '" ' +
              'data-borrow-id="' + borrow.id + '">Return Book</button>' +
              '</td>' +
              '<td>' +
              '<button type="button" class="btn btn-secondary delete-btn" data-borrower-id="' + borrow.id + '">Delete</button>' +
              '</td>' +
              '</tr>';
          tableBody.append(row);
      });
  }
});
