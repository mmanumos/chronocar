const user_id_panel = sessionStorage.getItem('UserID');
console.log("UserID: " + user_id_panel);
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
// Subcategories
$.ajax({
    url: 'http://34.71.55.165:5000/api/v1/users/'+ user_id_panel + '/categories_sub',
    type: 'GET',
    success: function (data) {
        console.log(data);
    },
    error: function () {
        console.log('error API connection');
    }
});
