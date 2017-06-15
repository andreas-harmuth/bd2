//var ohm = [1666.7, 1304.3, 909.1, 740.7, 654.2, 566.0, 476.2, 430.6, 384.6, 338.2, 291.3, 243.9, 196.1, 147.8, 99.0, 1666.7, 1304.3, 909.1, 740.7, 654.2, 566.0, 476.2, 384.6, 338.2, 291.3, 243.9, 196.1, 147.8, 99.0, 79.4, 69.5, 909.1, 740.7, 654.2, 566.0, 476.2, 384.6, 291.3, 243.9, 196.1, 147.8, 99.0, 79.4, 69.5, 59.6, 49.8, 196.1, 147.8, 118.6, 99.0, 89.2, 79.4, 69.5, 59.6, 49.8, 39.8, 29.9, 99.0, 79.4, 69.5, 59.6, 49.8, 39.8, 29.9, 79.4, 69.5, 59.6, 49.8, 39.8, 29.9, 20.0, 15.0, 10.0, 74.4, 69.5, 64.6, 54.7, 49.8, 44.8, 39.8, 34.9, 29.9, 24.9, 20.0, 15.0, 10.0, 44.8, 39.8, 34.9, 29.9, 24.9, 20.0, 15.0, 10.0, 8.0, 7.0, 6.0, 5.0, 34.9, 29.9, 25.9, 22.9, 20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 32.9, 29.9, 27.9, 25.9, 23.9, 22.0, 20.0, 18.0, 16.0, 14.0, 12.0, 10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0];
//var power = [0.6289, 0.6393, 0.6779, 0.7109, 0.7203, 0.753, 0.7804, 0.7738, 0.8078, 0.8284, 0.8357, 0.8604, 0.8328, 0.8013, 0.6557, 0.9021, 0.9465, 0.9845, 1.007, 1.0251, 1.0683, 1.1098, 1.1593, 1.1898, 1.2415, 1.2735, 1.2709, 1.2864, 1.2651, 1.1722, 1.1359, 1.2966, 1.343, 1.391, 1.4473, 1.522, 1.6028, 1.7424, 1.8062, 1.9184, 2.0553, 2.1808, 1.9531, 1.8503, 1.8564, 1.7393, 2.5519, 2.7899, 2.9236, 3.0162, 3.1313, 3.1903, 3.242, 3.2933, 3.0642, 2.7051, 2.5342, 4.1423, 4.222, 4.3831, 4.5022, 4.5814, 4.631, 4.0545, 5.4665, 5.5409, 5.8113, 5.9928, 6.0798, 5.9285, 6.0173, 5.2842, 4.7139, 6.9232, 7.0908, 7.1222, 7.3035, 7.5929, 7.6214, 7.5914, 7.6417, 7.6493, 7.8074, 7.7703, 7.7271, 7.3295, 8.8912, 9.1239, 9.1881, 9.2197, 9.2274, 9.2316, 9.2838, 9.5491, 9.0742, 9.4592, 9.2702, 9.0815, 10.5275, 10.7383, 10.5661, 10.7514, 10.8185, 10.9471, 10.8398, 10.7914, 10.8328, 11.0214, 10.9237, 10.85, 10.811, 10.8243, 10.9226, 10.0005, 10.1644, 12.2461, 12.3725, 12.3628, 12.3911, 12.4675, 12.3338, 12.531, 12.5106, 12.567, 12.334, 12.1546, 12.0615, 12.0659, 12.1219, 12.2529, 12.4987, 11.9067, 12.4097, 11.7365, 11.8852];
//var wind = [6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 13.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0];


var isValid = false;


$('#submit').click(function () {

    const ohm = $('#res').val().split(",");
    const power = $('#p').val().split(",");
    const wind = $('#ws').val().split(",");
    const sort_list = ($('#sl').val() === "" ? [-1] : $('#sl').val().split(","));
    const type = $('#splitType').dropdown('get value');


    $.ajax({
        url: '/api/sort_3d_data',
        data: {'data':JSON.stringify({"ohm":ohm,"power":power,"wind":wind,"sort_list":sort_list,"type":type})},
        type: 'POST',
        success: function(res) {
            graphVal = JSON.parse(res).graph;

            var data = [];

            for(data_max in graphVal){

                data.push({
                x: graphVal[data_max].ohm,
                y: graphVal[data_max].wind,
                z: graphVal[data_max].power,
                name:data_max,
                mode: 'markers',
                marker: {
                    size: 3,
                    line: {
                    color: 'rgba(217, 217, 217, 0.14)',
                    width: 0.5},
                    opacity: 0.8},
                type: 'scatter3d'
            });
            }

            // Plotting the mesh

            var layout = {margin: {
                l: 0,
                r: 0,
                b: 0,
                t: 0
              },
                scene: {
                yaxis: {
                    title: 'Wind speed (m/s)'
                  },
                xaxis: {
                    title: 'Ohm'
              },
                zaxis: {
                    title: 'Power (W)'
              }}
            };
            Plotly.newPlot('myDiv', data,layout);
        },
        error: function (err) {
            console.log(err)
        }
});


});
$('#dataName').keyup(function () {

    const name = ($(this).val() === "" ? "noname" : $(this).val());

    $.ajax({
        url: '/api/namecheck',
        data: {
            'data':JSON.stringify({"name":name,
            'group_number': $('#grpNumber').val()})
        },
        type: 'POST',
        success: function (res) {
            isValid = JSON.parse(res).isValid;

            if(isValid && $('#grpNumber').val() !== "Group number" && $('#grpNumber').val() !== null) {
                $('#addGraph').removeClass('disabled')
            }
            else{
                $('#addGraph').addClass('disabled')
            }

        },
        error: function (err) {
            console.log(err)
        }
    });
});

$('#grpNumber').change(function () {

    const name = ($('#dataName').val() === "" ? "noname" : $('#dataName').val());
    console.log(name);
    $.ajax({
        url: '/api/namecheck',
        data: {
            'data':JSON.stringify({"name":name,
            'group_number': $(this).val()})
        },
        type: 'POST',
        success: function (res) {
            isValid = JSON.parse(res).isValid;

            if(isValid && $('#grpNumber').val() !== "Group number" && $('#grpNumber').val() !== null) {
                $('#addGraph').removeClass('disabled')
            }
            else{
                $('#addGraph').addClass('disabled')
            }

        },
        error: function (err) {
            console.log(err)
        }
    });

});

$('#addGraph').click(function () {
    const ohm = $('#res').val().split(",");
    const power = $('#p').val().split(",");
    const wind = $('#ws').val().split(",");
    const groupNumber = $('#grpNumber').val();
    const name = $('#dataName').val();

    $.ajax({
        url: '/api/addGraph',
        data: {
            'data':JSON.stringify({"wind":wind,
            'res': ohm,
            'power': power,
            'name':name,
            'group_number':groupNumber})
        },
        type: 'POST',
        success: function (res) {
            location.reload();

        },
        error: function (err) {
            console.log(err)
        }
    });
});

var fetchData = function (name,groupNumber) {


    $.ajax({
        url: '/api/databyid',
        data: {
            'data':JSON.stringify({"name":name,
            'group_number': groupNumber})
        },
        type: 'POST',
        success: function (res) {
            data = JSON.parse(res).data;

            $('#ws').val(data.wind);
            $('#res').val(data.res);
            $('#p').val(data.power);
        },
        error: function (err) {
            console.log(err)
        }
    });


};
