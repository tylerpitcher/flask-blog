$(document).ready(function() {
    // When a delete btn is clicked make delete request to '/remove'.
    $('.delete-btn').each(function() {
        $(this).click(function() {
            $.ajax({
                data: {
                    hash: $(this).val()
                },
                type: 'DELETE',
                url: '/remove'
            }).done(function() {
                location.reload();
            });
        });
    });
});