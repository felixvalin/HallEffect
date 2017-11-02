#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:02:56 2017

@author: felix
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import thermocouple as tc
import spinmob as s

#Font size!
font = {'family' : 'normal',
        'size'   : 15}

matplotlib.rc('font', **font)

cooling_path = "../database/cooling_nitrogen_0p174/cooling_nitrogen.txt"
heating_path = "../database/noheat_31102017/0p124V_hallangle296_150K.txt"

#alpha = -5.0
#beta = 0.5276
#current = 0.001 #Amps
##bfield = -((np.float(filepath.split("/")[-1].split("_")[0])*1000-alpha)/beta)/1000
#ebfield = 0.024/beta

l5, el5 = np.load("../database/distance_v5.npy")
d, ed = np.load("../database/d_sample.npy")
w, ew = np.load("../database/w_sample.npy")

cooling_data = s.data.load(cooling_path)
heating_data = s.data.load(heating_path)

thermo = tc.Thermocouple()

cooling_volt = -1*cooling_data['v5']
heating_volt = -1*heating_data['v5']

cooling_temperature = thermo.toKelvin(cooling_data['v8'])
heating_temperature = thermo.toKelvin(heating_data['v8'])

def resistivity(v5):
    l5, el5 = np.load("../database/distance_v5.npy")
    d, ed = np.load("../database/d_sample.npy")
    w, ew = np.load("../database/w_sample.npy")
    
    el5 *= 0.1
    
    I = 0.001
    
    res = np.zeros(len(v5))
    eres = np.zeros(len(v5))
    
    for i in range(len(v5)):
        res[i] = v5[i]*w*d/(I*l5)
        eres[i] = np.sqrt((v5[i]*w*ed/(I*l5))**2 + (v5[i]*ew*d/(I*l5))**2 + (v5[i]*w*d*el5/(I*l5**2))**2)
    
    return res, eres
      
cooling_res, cooling_eres = resistivity(cooling_volt)  
heating_res, heating_eres = resistivity(heating_volt) 

plt.figure()
plt.errorbar(cooling_temperature, cooling_res, yerr=cooling_eres, fmt='k.', capsize=2, markersize=2, errorevery=5, label="Cooling")
plt.errorbar(heating_temperature, heating_res, yerr=heating_eres, fmt='b.', capsize=2, markersize=2, errorevery=10, label="Heating")
plt.xlim(150,295)
plt.legend(loc=4)
plt.xlabel("Temperature [K]")
plt.ylabel("Resistivity [$\Omega$ mm]")
plt.savefig("../assets/figures/cooling_heating_150K_295K.png")
plt.show()
plt.close()

new_res = np.append(cooling_res, heating_res)
new_eres = np.append(cooling_eres, heating_eres)
new_temp = np.append(cooling_temperature, heating_temperature)

fitter = s.data.fitter('a*x**(3/2)+b', 'a,b')
fitter.set_data(xdata=new_temp, ydata=new_res, eydata=new_eres)
fitter.set(coarsen=3, xlabel="Temperature [K]", ylabel="Resistivity [$\Omega$ mm]")
#fitter.fit(xmax=295, coarsen=5)
fitter.fit(xmin=175, xmax=250, coarsen=2)

#lower_fitter = s.data.fitter(f=['a*x**(3/2)+b'], p='a,b')
#lower_fitter.set_data(xdata=temperature, ydata=res, eydata=eres)
#lower_fitter.set(coarsen=3, xlabel="Temperature [K]", ylabel="Resistivity [$\Omega$ mm]")
#lower_fitter.fit(xmax=300)
#lower_fitter.ginput()
#plt.savefig("../assets/figures/lower_resistivity.svg")
#plt.close()
#
#upper_fitter = s.data.fitter(f=['c*exp(d/x)'], p='c,d')
#upper_fitter.set_data(xdata=temperature, ydata=res, eydata=eres)
#upper_fitter.set(coarsen=2, xlabel="Temperature [K]", ylabel="Resistivity [$\Omega$ mm]")
#upper_fitter.fit(xmin=350)
#upper_fitter.ginput()
#plt.savefig("../assets/figures/upper_resistivity.svg")
#plt.close()