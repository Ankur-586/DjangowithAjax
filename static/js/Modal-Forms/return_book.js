$(document).ready(function() {
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    
    $('#returnModal').on('show.bs.modal', function(event) {
      var button = $(event.relatedTarget);
      var studentId = button.data('student-id');
      var returnDate = button.data('return-date');
      var borrowId = button.data('borrow-id')
      console.log(borrowId,returnDate,studentId)

      $.ajax({
        url: returnbookUrl,
        method: 'GET',
        data: {
          'student-id': studentId, // Pass student ID as GET parameter
          'borrow-id': borrowId // Pass borrow ID as GET parameter
        },
        headers: { "X-CSRFToken": csrftoken },
        success: function(response) {
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

      // Close the modal
      //$('#returnModal').modal('hide');

      // Send AJAX request to the Django view
      $.ajax({
          url: returnbookUrl.replace('0', studentId).replace('0', borrow_id),
          type: 'POST',
          headers: { "X-CSRFToken": csrftoken },
          data: {
              'returnDate': returnDate // Include returnDate in the data
          },
          success: function(response) {
              // Display success message
              $('#successMessage').text(response.message);
              $('#successMessage').show().delay(2000).fadeOut('slow');
              // $('#returnModal').modal('hide');
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