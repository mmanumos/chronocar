const user_id_panel = sessionStorage.getItem('UserID');
console.log("UserID: " + user_id_panel);
//Alerts panel
const url_mileage = 'http://34.71.55.165:5000/api/v1/users/' + user_id_panel + '/mileage/';
$.ajax({
    url: url_mileage,
    type: 'GET',
    success: function (data) {
        let last_mileage = data['mileage'];
        //last mileage
        $("#last_mileage").text(last_mileage);
    },
    error: function () {
        console.log('error API connection');
    }
});


//Alerts panel
const url_panel = 'http://34.71.55.165:5000/api/v1/users/' + user_id_panel + '/alerts/panel/';
$.ajax({
    url: url_panel,
    type: 'GET',
    success: function (data) {
        let total = 0;
        for (var i = 0; i < data.length; i++) {
            let state = "";
            if (data[i]['color'] == 'green') {
                state = "<i class='fas fa-circle text-success'></i>";
            } else if (data[i]['color'] == 'orange') {
                state = "<i class='fas fa-circle text-warning'></i>";
            } else {
                state = "<i class='fas fa-circle text-danger'></i>";
            }
            $('#alerts_panel').append('<tr> <td>' + data[i]['missing'] + '</td> <td>' + state + '</td> <td>' + data[i]['catsub_name'] + '</td>  </tr>');
        }
    },
    error: function () {
        console.log('error API connection');
    }
});