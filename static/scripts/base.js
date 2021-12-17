$(document).ready(function () {
    $('#filelist a').on('click', function () {
        let txt = ($(this).text());
        document.getElementById('selectedfile').value = txt;

    });
});

$(document).ready(function () {
    $('#header-list a').on('click', function () {
        let txt = ($(this).text());
        document.getElementById('selected-header').value = txt;

    });
});


$(document).ready(function () {
    $("#exampleModal").modal('show');
});



