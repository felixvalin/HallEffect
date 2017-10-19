#!/usr/bin/env python3
import spinmob as s
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob
import os

def find_max(W, B):
    w, ew = W
    b, eb = B
    
    x_max = (3*np.pi/2+b)/w
    ex_max = np.sqrt((eb/w)**2 + (-b*ew/w**2)**2)
    
    print("Hall Angle")
    print("{0:0.2f} +/- {1:0.2f} [rad]".format(x_max, ex_max))
    print("{0:0.2f} +/- {1:0.2f} [deg]".format(np.rad2deg(x_max), np.rad2deg(ex_max)))
    
    np.save("hallAngle.npy", [np.rad2deg(x_max), np.rad2deg(ex_max)])    
    
    return x_max, ex_max

#Font size!
font = {'family' : 'normal',
        'size'   : 15}
 
matplotlib.rc('font', **font)

#datasets = s.data.load_multiple("../database/hall_angle/*")

#Voltage error........ arbitrary or given ???
err_volt = 0.01
err_volt *= np.sqrt(2)

os.chdir("../database/hall_angle/")

paths = glob.glob("*.txt")

angles = np.zeros(len(paths))
volt_diffs = np.zeros((2,len(paths)))

for i, path in enumerate(paths):
    d = s.data.load(path)
    #times = d['time']
    angles[i] = np.deg2rad(int(path.split('_')[0]))
    v1_mean = np.mean(d['v1'])
    v1_std = np.std(d['v1'])
    v2_mean = np.mean(d['v2'])
    v2_std = np.std(d['v2'])

    volt_diffs[0][i] = v2_mean - v1_mean
    volt_diffs[1][i] = np.sqrt(v1_std**2+v2_std**2)
        
    #volt_diff = d['v2'] - d['v1']
#    print("Done with iteration {}".format(i))

fitter = s.data.fitter(f='a*sin(w*x-b)+c', p='a=0.005, w=1, b=1, c=0')
fitter.set_data(xdata=angles, ydata=volt_diffs[0], eydata=volt_diffs[1])
fitter.fit()
fitter.set(plot_guess=False)
#fitter.trim
plt.xlabel('Angle [rad]')
plt.ylabel('Voltage Difference [V]')
plt.savefig('../../assets/figures/hall_angle_fit.svg')
plt.show()
#fitter.ginput()
plt.close()


results = np.zeros((4,2)) #Number of parameters

for i in range(len(results)):
    results[i]=[fitter.results[0][i],fitter.results[1][i][i]]
  
#print(np.rad2deg((3*np.pi/2+results[2][0])/results[1][0]))
#print((np.pi/2+results[2][0])/results[1][0])
    


find_max(results[1], results[2])
