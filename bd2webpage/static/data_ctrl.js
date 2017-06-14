
var data_input = {
            wind: [],
            voltage: []
        };

var groupNo = 0;


readFile = function () {
    var dfrd1 = $.Deferred();
    var reader = new FileReader();
    reader.onload = function () {

        // Split the list into datapoints
        //TODO: fix this for win?
        csv_list = reader.result.split("\r\n");

        // Identify the data separator
        if(csv_list[0].split(",").length > 1){
            var split_sym = ",";
        }
        else if(csv_list[0].split(";").length > 1){
            var split_sym = ";";
        }
        else{
            alert('It seems the separator you are using is not supported. Please choose between: \",\" or \";\"');
            split_sym = null;
        }

        for(var i=0; i < csv_list.length;i++){
            data_input.wind.push(csv_list[i].split(split_sym)[0]);
            data_input.voltage.push(csv_list[i].split(split_sym)[1]);
        }

        dfrd1.resolve();



    };
    // start reading the file. When it is done, calls the onload event defined above.

    reader.readAsBinaryString(document.getElementById("csv").files[0]);

    return dfrd1.promise();
};

$(function () {
    $('.dropdown-menu li').click(function () {
        groupNo = parseInt($(this).text());

        $.ajax({
                url: '/api/groupdata',
                data: {'group_number':groupNo},
                type: 'POST',
                success: function(res) {
                    params = JSON.parse(res);
                    if(params.found === false){
                        console.log('No data found')
                    }
                    else{
                        $('#innerR').val(params.innerR);
                        $('#flux').val(params.flux);
                        $('#a').val(params.a);
                        $('#b').val(params.b);
                        $('#c').val(params.c);
                        $('#fan_size').val(params.fan_size);
                    }
                    $('#groupTitle').text('for group ' + groupNo)
                },
                error: function(err) {

                    alert(err);

                }
        }).done(function () {
            $('#chooseGroupDiv').slideUp();
            $('#groupDataIn').slideDown()
        })

    })
});


$(function() {
    $('#submitData').click(function() {
        params = {'group_number':groupNo};
        $('input').each(function () {
           if($(this).attr('id') != 'csv'){
               params[$(this).attr('id')] = $(this).val()

           }
        });

        readFile().done(function () {

                $.ajax({
                url: '/api/graphdata',
                data: {'data':JSON.stringify(data_input),
                'params':JSON.stringify(params)},
                type: 'POST',
                success: function(res) {
                    graphVal = JSON.parse(res).graph;
                    og_grapVal = JSON.parse(res).ogData;

                    var gData = {
                        x: graphVal.wind,
                        y: graphVal.power,
                        mode: 'lines+markers',
                        type: 'scatter',
                        name: 'Processed test data'
                    };
                    var ogData = {
                        x: og_grapVal.wind,
                        y: og_grapVal.power,
                        mode: 'lines+markers',
                        type: 'scatter',
                        name: 'Original test data'
                    };

                    var layout = {
                      title: 'True power output',
                      xaxis: {
                        title: 'Wind speed (m/s)'
                      },
                      yaxis: {
                        title: 'Power W'
                      }
                    };

                    var data = [gData,ogData];

                    Plotly.newPlot('chartPower', data,ogData,layout);





                    var cpData = {
                        x: graphVal.wind,
                        y: graphVal.cp,
                        mode: 'lines+markers',
                        type: 'scatter',
                        name: 'Processed test data'
                    };

                    // Betz limit 59%
                    var cBetz = {
                          x: [Math.min.apply(null,graphVal.wind),Math.max.apply(null,graphVal.wind)],
                          y: [0.59,0.59],
                          mode: 'lines',
                          name: 'Betz limit',
                          line: {
                            dash: 'dot',
                            width: 4
                          }
                        };


                    var cLayout = {
                      title: 'Efficiency of blade',
                      xaxis: {
                        title: 'Wind speed (m/s)'
                      },
                      yaxis: {
                          title: 'Cp',
                          range: [0, 1],
                          autorange: false

                      }
                    };

                    var cData = [cpData,cBetz];
                    $('#graphContainer').slideDown();
                    Plotly.newPlot('chartCp', cData,cLayout);

                    data_input = {wind: [], voltage: []};

                },
                error: function(err) {

                    alert(err);
                    data_input = {wind: [], voltage: []};

                }
            });


        });



    });
});

