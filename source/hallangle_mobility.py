#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:53:39 2017

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

hall1 = d['v1']# - 0.024 #Hall voltage
hall2 = d['v2']# - 0.024 #Hall voltage
hall = hall2 - hall1
v5 = d['v5']
hallangle = -hall1/v5
epercent = 0.0009/100#percent!
#epercent = 0.009
ehallangle = np.sqrt((epercent*hall/v5)**2 + (epercent*v5*hall/v5**2)**2)
ehallangle = epercent*hallangle
temperature = thermo.toKelvin(d['v8'])

plt.figure()
#plt.errorbar(temperature, Rh, yerr=eRh, fmt='.', errorevery=5, elinewidth=0.5, markersize=2, capsize=1)
plt.errorbar(temperature, hallangle, yerr=ehallangle, fmt='.', errorevery=2, elinewidth=0.5, markersize=2, capsize=1)
plt.xlabel("Temperature [K]")
plt.ylabel("Hall Angle (B-Field: {0:0.2f} T)".format(bfield))
#plt.savefig("../assets/figures/Angle_Temp.svg")
#plt.savefig("../assets/figures/Angle_Temp.png")
plt.show()