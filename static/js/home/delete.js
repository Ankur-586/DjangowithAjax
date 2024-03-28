$(document).ready(function() {
    $('#tab4').on('click', '.delete-btn', function(event) {
        
        var borrowerId = $(this).data('borrower-id');
        var confirmation = confirm("Are you sure you want to delete this record?");

        if (confirmation !== true) {
            return false; // Explicitly return false on cancel
          }
          $.ajax({
            url: deleteBookUrl.replace('0', borrowerId),
            method: 'DELETE',
            headers: { "X-CSRFToken": csrftoken },
            success: function(response) {
                $('#errorMessage').delay(2000).text(response.message).show().fadeOut('slow');
                // Update the table after deletion
                updateTable();
            },
            error: function(xhr, status, error) {
                console.error('Error deleting borrower record:', error);
            }
        });
    });
});

// $(document).ready(function() {
//     $('.delete-btn').click(function() {
//         // Fetch the borrower ID associated with the clicked button
//         var borrowerId = $(this).data('borrower-id');
//         //console.log('Borrower ID:', borrowerId);
//         var csrftoken = $('input[name=csrfmiddlewaretoken]')[0].value;
//          $.ajax({
//              url: deleteBookUrl.replace('0', borrowerId),
//              headers: {
//                 'X-CSRFToken': csrftoken  // Include CSRF token in request headers
//             },
//              type: 'DELETE',
//              success: function(response) {
//                 $('#successMessage').delay(2000).text(response.message).show().fadeOut('slow');
//                 $('#borrowerRow_' + borrowerId).remove();
//              },
//              error: function(xhr, status, error) {
//                  // Handle error response
//              }
//          });
//     });
// });