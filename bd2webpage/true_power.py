

from math import pi

class Blade_test:
    def __init__(self,data_mes,wind,flux,a,b,c,r_inner,r_load,fan_size):
        sort_i = [i[0] for i in sorted(enumerate(wind), key=lambda x:x[1])]

        # Sort the data
        data_mes_i_sort = [None]*len(wind)
        for s_i,i in enumerate(sort_i):
            data_mes_i_sort[s_i]  = data_mes[i]



        self.wind = sorted(wind)
        self.data_mes = data_mes_i_sort
        self.flux = float(flux)
        self.a = a
        self.b = b
        self.c = c
        self.r_inner = r_inner
        self.r_load = r_load
        self.fan_size = fan_size

    def true_power(self,voltage_mes):
        voltage_gen = voltage_mes*(self.r_load+self.r_inner)/self.r_load
        omega = voltage_gen/self.flux
        inner_power = (voltage_mes/self.r_load)**2*self.r_inner
        actual_power = voltage_mes**2/self.r_load
        return inner_power + actual_power + self.a*omega**2+self.b*omega+self.c

    def cp(self,wind,tp):
        power_max = 1/2*1.2*(0.009+self.fan_size)**2*pi*wind**3
        return tp/power_max

    def graph(self):
        coord = {'wind':[],
                 'power':[],
                 'cp':[]}
        for data, wind in zip(self.data_mes, self.wind):
            tp = self.true_power(data)
            coord['power'].append(tp)
            coord['wind'].append(wind)
            coord['cp'].append(self.cp(wind,tp))



        return coord


