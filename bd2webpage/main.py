from flask import Flask, render_template,request
import json,pygal
from true_power import Blade_test as Bt
from db import BladeDB as Bdb
from pygal.style import Style
app = Flask(__name__)

db = Bdb('fooDB2')

@app.route('/')
def main_view():
    return render_template('main_data.html')




@app.route('/competition')
def comp_view():


    ########################### Style ############################
    custom_style = Style(
        background='transparent',
        plot_background='transparent',
        foreground_strong='#FFFFFF',
        opacity='.6',
        opacity_hover='.6',
        transition='400ms ease-in')


    ######################### Power graph #########################
    power_chart = pygal.XY(fill=False, interpolate='cubic', style=custom_style)
    power_chart.title = 'Power output from all groups'
    data_out = db.get_all_graph()
    for data in data_out:
        power_chart.add(data, [(float(wind),float(power)) for wind,power in zip(data_out[data]['wind'],data_out[data]['power'])])

    power_chart = power_chart.render_data_uri()


    ########################### CP graph ##########################
    cp_chart = pygal.XY(fill=False, interpolate='cubic', style=custom_style)
    cp_chart.title = 'Power output from all groups'
    for data in data_out:
        cp_chart.add(data, [(float(wind),float(cp)) for wind,cp in zip(data_out[data]['wind'],data_out[data]['cp'])])

    cp_chart = cp_chart.render_data_uri()


    ########################### Get winners ########################
    # group_number,test_date,test_id,wind,power,cp,inner_res,load_res,flux,eqa,eqb,eqc,blade_length
    power_winner, cp_winner = db.get_leaders()
    all_best = db.get_best()
    if cp_winner == None:
        return render_template('comp.html', power_chart=power_chart, cp_chart=cp_chart, all_best=all_best)

    else:
        return render_template('comp.html',power_chart=power_chart,cp_chart=cp_chart,all_best = all_best,
                               cgroup=cp_winner[0],
                               cdate=cp_winner[1][:19],
                               ctestNo=cp_winner[2],
                               cwindSpeed=cp_winner[3],
                               cpower=round(cp_winner[4],4),
                               ccp=round(cp_winner[5],3),
                               cinnerR=cp_winner[6],
                               cloadR=cp_winner[7],
                               cflux=cp_winner[8],
                               ca=cp_winner[9],
                               cb=cp_winner[10],
                               cc=cp_winner[11],
                               cbladeLength=cp_winner[12],
                               pgroup=power_winner[0],
                               pdate=power_winner[1][:19],
                               ptestNo=power_winner[2],
                               pwindSpeed=power_winner[3],
                               ppower=round(power_winner[4],4),
                               pcp=round(power_winner[5],4),
                               pinnerR=power_winner[6],
                               ploadR=power_winner[7],
                               pflux=power_winner[8],
                               pa=power_winner[9],
                               pb=power_winner[10],
                               pc=power_winner[11],
                               pbladeLength=power_winner[12]
                               )

@app.route('/api/graphdata',methods=['GET', 'POST'])
def main_data():

    # Get the data as a dict
    data = json.loads(request.form['data'])


    # convert the data from strings into float, this could might be avoided by not json.stringify it
    for i in range(len(data['wind'])):
        data['wind'][i] = float(data['wind'][i])
        data['voltage'][i] = float(data['voltage'][i])
    params = json.loads(request.form['params'])

    # Get params from the ajax call
    flux = float(params['flux'])
    r_inner = float(params['innerR'])
    r_load = float(params['loadR'])
    a = float(params['a'])
    b = float(params['b'])
    c = float(params['c'])
    fan_size = float(params['fan_size'])
    group_number = int(params['group_number'])

    #def __init__(self, data_mes, wind, flux, a, b, c, r_inner, r_load,fan_size):
    output = Bt(data['voltage'],data['wind'],flux, a, b, c, r_inner, r_load, fan_size)




    #def add_record(self,group_number,wind,power,cp,inner_res,load_res,flux,eqa,eqb,eqc,blade_length):
    db.add_record(group_number, output.graph()['wind'], output.graph()['power'], output.graph()['cp'], r_inner, r_load, flux, a, b, c, fan_size)


    return json.dumps({'graph':output.graph()})

@app.route('/api/groupdata',methods=['GET', 'POST'])
def group_data():
    # Get the entered group number
    group_number = json.loads(request.form['group_number'])


    # Get the params from the db
    params = db.fetch_group_params(group_number)

    # If the parameter is not found, let the controller know
    if params == None:
        return json.dumps({'found' : False})

    # Else retun the data
    return json.dumps({'found' : True,
                       'innerR' : params[1],
                       'flux' : params[2],
                       'a' : params[3],
                       'b' : params[4],
                       'c' : params[5],
                       'fan_size':params[6]})

if __name__ == '__main__':
    app.run()

