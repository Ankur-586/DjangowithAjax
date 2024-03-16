// $(document).ready(function(){
//     $('.nav-tabs a').click(function(e){
//         e.preventDefault();
//         $(this).tab('show');
//     });
// });

// $(document).ready(function() {
//     // Handle tab link clicks
//     $('.nav-tabs a').click(function(e) {
//         e.preventDefault(); // Prevent default link behavior
//         var tabId = $(this).attr('href'); // Get the target tab ID
//         $('.nav-tabs a').removeClass('active'); // Remove active class from all tab links
//         $(this).addClass('active'); // Add active class to the clicked tab link
//         $('.tab-pane').removeClass('show active'); // Remove show and active classes from all tab panes
//         $(tabId).addClass('show active'); // Add show and active classes to the target tab pane
//     });
// });

$(document).ready(function() {
    // Hide tabs initially
    $('.nav-tabs').hide();
    
    // Retrieve the active tab from local storage when the page loads
    var activeTab = localStorage.getItem('activeTab');
    if (activeTab) {
        $('a[href="' + activeTab + '"]').tab('show');
    }
    
    // Show tabs after retrieving the active tab from local storage
    $('.nav-tabs').fadeIn('fast');

    // Handle tab link clicks
    $('.nav-tabs a').click(function(e) {
        e.preventDefault(); // Prevent default link behavior
        var tabId = $(this).attr('href'); // Get the target tab ID
        $('.nav-tabs a').removeClass('active'); // Remove active class from all tab links
        $(this).addClass('active'); // Add active class to the clicked tab link
        $('.tab-pane').removeClass('show active'); // Remove show and active classes from all tab panes
        $(tabId).addClass('show active'); // Add show and active classes to the target tab pane
        
        // Store the active tab ID in local storage
        localStorage.setItem('activeTab', tabId);
    });
});
