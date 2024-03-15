$(document).ready(function() {
    $('.delete-btn').click(function() {
        // Fetch the borrower ID associated with the clicked button
        var borrowerId = $(this).data('borrower-id');
        console.log('Borrower ID:', borrowerId);
        var csrftoken = $('input[name=csrfmiddlewaretoken]')[0].value;
        var formData = {
            'csrfmiddlewaretoken': csrftoken,
        }
         $.ajax({
             url: deleteBookUrl.replace('0', borrowerId),
             headers: {
                'X-CSRFToken': csrftoken  // Include CSRF token in request headers
            },
             type: 'DELETE',
             success: function(response) {
                $('#successMessage').delay(2000).text(response.message).show().fadeOut('slow');
                $('#borrowerRow_' + borrowerId).remove();
             },
             error: function(xhr, status, error) {
                 // Handle error response
             }
         });
    });
});