// Get is used to verify if API
$.ajax({
    url: 'http://34.71.55.165:5000/api/v1/status',
    type: 'GET',
    success: function (data) {
        if (data.status == "OK") {
            console.log('GOOGLE CLOUD - API STATUS OK');
        }
    },
    error: function () {
        console.log('error API connection');
    }
});
// jQuery
$(document).ready(function () {
    $('#btnSignin').click(function () {
        const email = $(this).attr('email');
        const password = $(this).attr('password');
        $.ajax({
            url: 'http://34.71.55.165:5000/api/v1/users/login/',
            type: 'POST',
            data: $("#form-signin").serialize(),
            success: function (data) {
                console.log('Good!');
            },
            error: function () {
                console.log('Error')
            }
        });
    });
});