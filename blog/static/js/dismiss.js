$(document).ready(function() {
    // When a dismiss button is clicked remove the buttons parent.
    $('.dismiss-btn').click(function() {
        $(this).parent().remove();
    });
});