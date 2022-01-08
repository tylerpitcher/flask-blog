$(document).ready(function() {
    $('.content').on('keyup', function() {
        let length = $(this).val().length;
        $('.char-count').text(length);
    });
});