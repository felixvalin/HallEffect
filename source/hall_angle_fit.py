#!/usr/bin/env python3
import spinmob as s
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import os

#Font size!
font = {'family' : 'normal',
        'size'   : 15}
 
matplotlib.rc('font', **font)

#datasets = s.data.load_multiple("../database/hall_angle/*")

#Voltage error........ arbitrary or given ???
err_volt = 0.01
err_volt *= np.sqrt(2)

os.chdir("../database/hall_angle/")

paths = glob.glob("{}".format(file_path))

angles = np.zeros(len(paths))
volt_diffs = np.zeros((2,len(paths)[0]))

for i, path in enumerate(paths):
    d = s.data.load(path)
    #times = d['time']
    angles[i] = int(path.split()[1])
    v1_mean = np.mean(d['v1'])
    v1_std = np.std(d['v1'])
    v2_mean = np.mean(d['v2'])
    v2_std = np.std(d['v2'])

    volt_diffs[0][i] = v2_mean - v1_mean
    volt_diffs[1][i] = np.sqrt(v1_std**2+v2_std**2)
    #volt_diff = d['v2'] - d['v1']

fitter = s.data.fitter(f='a*x+b', p='a=1, b=0')
fitter.set_data(xdata=angles, ydata=volt_diffs[0], eydata=volt_diffs[1])
fitter.fit()
plt.xlabel('Angle [deg]')
plt.ylabel('Voltage Difference')
plt.savefig('../assets/figures/hall_angle_fit.svg')

