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
$('#btnSignin').click(function(){
    var email = $("#email").val();
    var password = $("#password").val();
    var user = {
            "email": email,
            "password": password
    };
    var url = "http://34.71.55.165:5000/api/v1/users/login/";
    $.ajax({
       type: "POST",
       url: url,
       data: JSON.stringify(user),
       ContentType: 'Application/json',
       success: function(result)
       {
         console.log(result);
       },
       error: function(myerror){
            console.log(myerror);
       }
    });
 });