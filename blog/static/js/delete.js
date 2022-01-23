$(document).ready(function() {
    $('.delete-btn').each(function() {
        $(this).click(function() {
            $.ajax({
                data: {
                    id: $(this).val()
                },
                type: 'DELETE',
                url: '/remove'
            }).done(function() {
                location.reload();
            });
        });
    });
});