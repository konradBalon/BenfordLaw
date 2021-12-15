$(document).ready(function () {
    $('#filelist a').on('click', function () {
        let txt = ($(this).text());
        document.getElementById('selectedfile').value = txt;

    });
});


$('#upload_form').submit(function (e) {
    $('#messages').removeClass('hide').addClass('alert alert-success alert-dismissible').slideDown().show();
    $('#messages_content').html('<h4>MESSAGE HERE</h4>');
    $('#modal').modal('show');
    e.preventDefault();
});


