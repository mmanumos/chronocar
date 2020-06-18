let userId;
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
// Login
$('#btnSignin').click(function () {
    let email = $("#email").val();
    let password = $("#password").val();
    let user = {
        "email": email,
        "password": password
    };
    let url = "http://34.71.55.165:5000/api/v1/users/login/";
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(user),
        ContentType: 'Application/json',
        success: function (result) {
            userId = result.id;
            sessionStorage.setItem('User ID', userId);
            const divUserId = document.getElementById('showUserId');
            console.log(userId);
            location.href = "panel";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});
// Create account
$('#btnCreateAccount').click(function () {
    let name = $("#name").val();
    let last_name = $("#last_name").val();
    let email = $("#email").val();
    let password = $("#password").val();
    let initial_mileage = $("#initial_mileage").val();
    let user = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "initial_mileage": initial_mileage
    };
    let url = "http://34.71.55.165:5000/api/v1/users/";
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(user),
        ContentType: 'Application/json',
        success: function (result) {
            userId = result.id;
            console.log(userId);
            location.href = "panel";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});