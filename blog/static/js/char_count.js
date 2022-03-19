$(document).ready(function() {
    // When new text is added to the input update character count.
    $('.content').on('keyup', function() {
        let length = $(this).val().length;
        $('.char-count').text(length);
    });
});