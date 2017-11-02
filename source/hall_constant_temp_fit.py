#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:27:40 2017

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

d = s.data.load(filepath)

thermo = tc.Thermocouple()

#hall = d['v1'] #Hall voltage
hall1 = d['v1'] - 0.024 #Hall voltage
hall2 = d['v2'] - 0.024 #Hall voltage
hall = hall2 - hall1
#hall = d['v2'] - 0.024 #Hall voltage
temperature = thermo.toKelvin(d['v8'])

def hall_coeff(hall, bfield, ebfield):
    ehall = 0.0009/100 #% accuracy 
    current = 0.001 #Amps
    d, ed = np.load("../database/d_sample.npy")
    
    Rh = np.zeros(len(hall))
#    Rh = []
    eRh = np.zeros(len(Rh))
#    eRh = Rh
    
    for i in range(len(hall)):
        Rh[i] = (hall[i]*d)/(current*bfield)
#        Rh.append((hall[i]*d)/(current*bfield))
        eA = (ehall*hall[i]*d/(bfield*current))**2
#        eA = 0
        eB = (hall[i]*ed/(bfield*current))**2
#        eB = 0
        eC = (hall[i]*d*ebfield**2/(bfield**2*current))**2
#        eC = 0
        
        eRh[i] = np.sqrt(eA+eB+eC)
        
    return Rh, eRh

Rh, eRh = hall_coeff(hall, bfield, ebfield)
#Rh = hall_coeff(hall, bfield, ebfield)

plt.figure()
#plt.plot(temperature, Rh, '.', markersize=3)
plt.errorbar(temperature, Rh, yerr=eRh, fmt='.', errorevery=5, elinewidth=0.5, markersize=2, capsize=1)
#plt.errorbar(temperature, hall, yerr=0.0001, fmt='.', errorevery=5, elinewidth=0.5, markersize=2)
plt.xlabel("Temperature [K]")
plt.ylabel("Hall Coefficient (B-Field: {0:0.2f} T)".format(bfield))
#plt.savefig("../assets/figures/Rh_Temp.svg")
#plt.savefig("../assets/figures/Rh_Temp.png")
plt.show()

#Rh_fitter = s.data.fitter(f="")
    
    