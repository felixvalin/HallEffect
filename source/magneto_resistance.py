#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 19:12:53 2017

@author: felix
"""


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import thermocouple as tc
import spinmob as s

#Font size!
font = {'family' : 'normal',
        'size'   : 15}

matplotlib.rc('font', **font)

def compute_b(v):
    bfields = np.zeros(len(v))
    for i in range(len(bfields)):
        alpha = -5.0
        beta = 0.5276
        bfields[i] = ((v[i]*1000-alpha)/beta)/1000
    return bfields

def resistivity(v5):
    l5, el5 = np.load("../database/distance_v5.npy")
    d, ed = np.load("../database/d_sample.npy")
    w, ew = np.load("../database/w_sample.npy")
    
#    el5 *= 0.1
    
    I = 0.001
    
    res = np.zeros(len(v5))
#    eres = np.zeros(len(v5))
    
    for i in range(len(v5)):
        res[i] = v5[i]*w*d/(I*l5)
#        eres[i] = np.sqrt((v5[i]*w*ed/(I*l5))**2 + (v5[i]*ew*d/(I*l5))**2 + (v5[i]*w*d*el5/(I*l5**2))**2)
    
    return res#, eres

filepath = "../database/magneto_resistance.txt"

current = 0.001 #Amps

d = s.data.load(filepath)

thermo = tc.Thermocouple()

#Compute mean and std of resistivity
voltage = -1*d['v5']
mean_voltage = np.mean(voltage.reshape(-1, 5), axis=1)
std_voltage = np.std(voltage.reshape(-1, 5), axis=1)

res = resistivity(mean_voltage)
eres = resistivity(std_voltage)
bfields = compute_b(d['volt'][0::5])

#mr_fitter = s.data.fitter('d*x**6+f*x**5+y*x**4+z*x**3+a*x**2+b*x+c', 'd,f,y,z,a,b,c')
#mr_fitter = s.data.fitter('y*x**4+z*x**3+a*x**2+b*x+c', 'y,z,a,b,c')
mr_fitter = s.data.fitter('a*x**2+b*x+c', 'a,b,c')
mr_fitter.set_data(xdata=bfields, ydata=res, eydata=eres)
mr_fitter.set(xlabel="Magnetic Field [T]", ylabel="Resistivity [$\Omega$ mm]", plot_guess=False)
#mr_fitter.fit(xmin=-0.3, xmax=0.3)
mr_fitter.fit(xmin=-0.25, xmax=0.25)
plt.ylim(43.05)
#plt.savefig("../assets/figures/magneto_resistance.png")
plt.savefig("../assets/figures/magneto_resistance.svg")
#mr_fitter.fit(xmin=-0.2, xmax=0.2)
#mr_fitter.fit()

#
#plt.figure()
#
##plt.errorbar(temperature, Rh, yerr=eRh, fmt='.', errorevery=5, elinewidth=0.5, markersize=2, capsize=1)
#plt.errorbar(bfields, res, yerr=eres, fmt='.', errorevery=1, elinewidth=0.5, markersize=2, capsize=3, capthick=0.5)
#plt.xlabel("Magnetic Field [T]")
#plt.ylabel("Resistivity [$\Omega$ mm]")
##plt.grid(True)
##plt.xscale('log')
##plt.yscale('log')
#plt.savefig("../assets/figures/magneto_resistance.svg")
#plt.savefig("../assets/figures/magneto_resistance.png")
#plt.show()