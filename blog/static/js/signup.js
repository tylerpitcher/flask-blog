function send_request(callback) {
    $.ajax({
        data: {
            email: $('#email').val(),
            username: $('#username').val(),
            password1: $('#password1').val(),
            password2: $('#password2').val()
        },
        type: 'POST',
        url: '/signup/verify'
    }).done(callback);
}

$(document).ready(function() {
    $('form').submit(function(event) {
        send_request(function(data) {
            let ready = Boolean(
                data.email
                && data.username
                && data.password1
                && data.passwords_match
            );
            
            if (!ready) event.preventDefault();
        });
    })

    $('#stage2').css('background-color', 'white');
    $('#stage3').css('background-color', 'white').css('border-color', 'transparent');

    $('#next1').click(function() {
        send_request(function (data) {
            if (data.email) {
                $('#stage2').css('background-color', '#00CAFF');
                $('#stage3').css('border-left-color', '#00CAFF');
                $('#form-section-1').css('display', 'none');
                $('#form-section-2').css('display', 'block');
            }
        });
    });

    $('#next2').click(function() {
        send_request(function (data) {
            if (data.email && data.username && data.password1 && data.passwords_match) {
                $('#stage3').css('background-color', '#53FF00')
                $('#form-section-2').css('display', 'none');
                $('#form-section-3').css('display', 'block');
            }
        });
    });
});