





$('.btn-select').click(function () {
    id_val = $(this).val();
    $('#select'+id_val).addClass('active');
    $('#graph' + id_val).show();
    for(var i = 0; i < 3;i++) {
        if (i != id_val) {
            $('#select' + i).removeClass('active');
            $('#graph' + i).hide();
        }

    }

});
$('#headerLead').click(function () {
   $('#currentLeadDiv').slideToggle()
});