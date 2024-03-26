$(document).ready(function() {
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    
    $('#returnModal').on('show.bs.modal', function(event) {
        var button = $(event.relatedTarget);
        var studentId = button.data('student-id');
        var returnDate = button.data('return-date');
        var borrowId = button.data('borrow-id');
        console.log(borrowId, returnDate, studentId)

        // AJAX request to get late penalty
        $.ajax({
            url: returnbookUrl,
            method: 'GET',
            data: {
                'student-id': studentId, // Pass student ID as GET parameter
                'borrow-id': borrowId // Pass borrow ID as GET parameter
            },
            headers: { "X-CSRFToken": csrftoken },
            success: function(response) {
                if (response && response.fine !== undefined) {
                    $('#lateFineContent').html('Total Fine: ' + '₹ ' + response.fine);
                } else {
                    $('#lateFineContent').html('Total Fine: 0'); // If fine is undefined, set it to 0
                }
            },
            error: function(xhr, status, error) {
                console.error(error);
                // Handle error here
            }
        });

        // Handle form submission
        $('#return_date').click(function(event) {
            var returnDate = $('#returnDate').val();
            
            // AJAX request to update return date
            $.ajax({
                url: returnbookUrl,
                type: 'POST',
                headers: { "X-CSRFToken": csrftoken },
                data: {
                    'student-id': studentId,  // Include student ID in the data
                    'borrow-id': borrowId,  // Include borrow ID in the data
                    'returnDate': returnDate // Include return date in the data
                },
                success: function(response) {
                    if ($('#successMessage').length) {
                        $('#successMessage').text(response.message);
                        $('#successMessage').show().delay(2000).fadeOut('slow');
                    } else {
                        console.error("Element with ID 'successMessage' not found.");
                    }
                },
                error: function(xhr, status, error) {
                    console.error("Error:", error);
                    // Handle error here
                }
            });
        });
    });
});
