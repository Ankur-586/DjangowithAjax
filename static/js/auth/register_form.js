$(document).ready(function() {
    // Function to toggle branch field visibility
    function toggleBranchFieldVisibility(role) {
        if (role === '1' || role === '') {
            $('#branchField').hide(); // Hide branch field for admin or when no role is selected
        } else {
            $('#branchField').show(); // Show branch field for other roles
        }
    }

    // Trigger function on role change
    $('#role').change(function() {
        var selectedRole = $(this).val();
        console.log('Selected Role:', selectedRole); // Print selected role to console
        toggleBranchFieldVisibility(selectedRole);
    });

    // Call function on page load to set initial visibility
    var initialRole = $('#role').val();
    console.log('Initial Role:', initialRole); // Print initial role to console
    toggleBranchFieldVisibility(initialRole);

    // Form submission AJAX
    $('#myForm').submit(function(event) {
        event.preventDefault();
        $.ajax({
            url: register_url,
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#successMessage').delay(2000).text(response.message).show().fadeOut('slow');
                $('#myForm')[0].reset();
            },
            error: function(xhr, status, error) {
                var errors = xhr.responseJSON.errors;
                if (errors) {
                    $.each(errors, function(field, messages) {
                        $('#' + field + '_errors').text(messages.join(' '));
                    });
                } else {
                    console.error("Error:", xhr.responseText);
                }
            }
        });
    });
});
