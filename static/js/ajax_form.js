$(document).ready(function () {
    $('#submitButton').click(function (event) {
        event.preventDefault();

        var allFieldsFilled = true;
        $('#myForm input, #myForm select, #myForm textarea').each(function (index, element) {
            if (!$(this).val().trim()) {
                allFieldsFilled = false;
                $('#errorMessage').text("One or More Fields are empty").show().delay(2000).fadeOut('slow');
                return false; // Exit the loop after showing the first error message
            }
        });

        if (allFieldsFilled) {
            var formData = new FormData($('#myForm')[0]);
            $.ajax({
                url: contactFormUrl,
                type: 'POST',
                data: formData,
                contentType: false,
                processData: false,
                success: function (response) {
                    $('#successMessage').text(response.message).show().delay(2000).fadeOut('slow');
                    $('#myForm')[0].reset();
                },
                error: function (xhr, status, error) {
                    var errorMessage = xhr.responseJSON.error;
                    if (errorMessage) {
                        $('#validationerror').text(errorMessage).show().delay(2000).fadeOut(3000);
                    } else {
                        console.error("Error:", xhr.responseText);
                        //$('#servererror').text(xhr.responseText).show().delay(2000).fadeOut(3000);
                    }
                }
            });
        }
    });
});