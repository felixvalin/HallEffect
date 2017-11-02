#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:56:57 2017

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

filepath = "../database/nitrogen_Bfield_261017/0.214_290_180K.txt"

alpha = -5.0
beta = 0.5276
current = 0.001 #Amps
bfield = -((np.float(filepath.split("/")[-1].split("_")[0])*1000-alpha)/beta)/1000
ebfield = 0.024/beta

l5, el5 = np.load("../database/distance_v5.npy")
d, ed = np.load("../database/d_sample.npy")
w, ew = np.load("../database/w_sample.npy")

data = s.data.load(filepath)

thermo = tc.Thermocouple()

v5 = -1*data['v6']

epercent = 0.0009/100#percent!

temperature = thermo.toKelvin(data['v8'])

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
      
res, eres = resistivity(v5)  

lower_fitter = s.data.fitter(f=['a*x**(3/2)+b'], p='a,b')
lower_fitter.set_data(xdata=temperature, ydata=res, eydata=eres)
lower_fitter.set(coarsen=3, xlabel="Temperature [K]", ylabel="Resistivity [$\Omega$ mm]")
lower_fitter.fit(xmax=300)
lower_fitter.ginput()
plt.savefig("../assets/figures/lower_resistivity.svg")
plt.close()

upper_fitter = s.data.fitter(f=['c*exp(d/x)'], p='c,d')
upper_fitter.set_data(xdata=temperature, ydata=res, eydata=eres)
upper_fitter.set(coarsen=2, xlabel="Temperature [K]", ylabel="Resistivity [$\Omega$ mm]")
upper_fitter.fit(xmin=350)
upper_fitter.ginput()
plt.savefig("../assets/figures/upper_resistivity.svg")
plt.close()