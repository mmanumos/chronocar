//Alerts panel
const user_id_alert = sessionStorage.getItem('UserID');

const url_alerts_settings = 'http://34.71.55.165:5000/api/v1/users/' + user_id_alert + '/alerts/settings/';
//const url_alerts_settings = 'http://0.0.0.0:5001/api/v1/users/' + user_id_alert + '/alerts/settings/';

$.ajax({
    url: url_alerts_settings,
    type: 'GET',
    success: function (data) {
        let total = 0;
        for (var i = 0; i < data.length; i++) {
            let state = '';
            $('#list_alerts').append(
                "<p style='font-weight:bold; font-size:20px; text-align:center' > " + data[i]['catsub_name'] + "</p > <div> <table class='table table-dark' class='dropdown-item'> <thead> <tr> <th scope='col'>Limit</th> <th scope='col'>High <i class='fas fa-circle text-danger'></i></th> <th scope='col'>Middle <i class='fas fa-circle text-warning'></i></th> <th scope='col'>Low <i class='fas fa-circle text-success'></i></th> </tr> </thead> <tbody> <tr> <td> " + data[i]['limit'] + "</td> <td> " + data[i]['high'] + "</td> <td> " + data[i]['middle'] + "</td> <td> " + data[i]['low'] + " </td> </tr> <tr> <td> <button type='button' class='btn btn-primary'> <span class='glyphicon glyphicon-trash'>Update </button> </td> </tr> <tr> <td> <button type='button' class='btn btn-secondary'> <span class='glyphicon glyphicon-trash'>Delete </button> </td> </tr> </tbody> </table> </div>"
            )
        }
    },
    error: function () {
        console.log('error API connection');
    }
});