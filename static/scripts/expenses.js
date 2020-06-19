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

const user_id = sessionStorage.getItem('UserID');
console.log("UserID: " + user_id);
const url = 'http://34.71.55.165:5000/api/v1/users/' + user_id + '/expenses/';

$.ajax({
    url: url,
    type: 'GET',
    success: function (data) {
        let total = 0;
        for (var i = 0; i < data.length; i++) {
            $('#table-expenses').append('<tr> <td>' + data[i]['created_at'] + '</td> <td>' + data[i]['catsu_name'] + '</td> <td>' + data[i]['amount'] + '</td>  </tr>');
            total = total + data[i]['amount'];
        }
        //Total expenses for user
        $("#total_expense").text("Total $" + total);
        const d = new Date()
        const ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d)
        const mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d)
        const da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d)
        $("#date_act_expense").text(da + "-" + mo + "-" + ye);
    },
    error: function () {
        console.log('error API connection');
    }
});