# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""Time is MISSING"""

#git add -A && git commit -a -m "new update of Hall Angle" && git push origin


import keithley
import time as t
import numpy as np
import spinmob as s
import thermocouple as tc
#import os

#import os
#clear = lambda: os.system('clear')
#clear()

dmm= keithley.DMM()
#print(dmm.about())
#
#keithley.monitor(dmm)
#
#dmm.get_voltage(8)

def get_h():
    return dmm.get_voltage(2)#Might be channel 1
def get_e():
    return dmm.get_voltage(1)#Might be channel 2
def get_hall():
    return dmm.get_voltage(3)
def get_v4():
    return dmm.get_voltage(4)
def get_v5():    
    return dmm.get_voltage(5)
def get_v6():    
    return dmm.get_voltage(6)
def get_v7():    
    return dmm.get_voltage(7)
def get_temp():
    return dmm.get_voltage(8)


def get_allVoltages():
    return get_h(),get_e(),get_hall(),get_v4(),get_v5(),get_v6(),get_v7(),get_temp()

def retreive_hall(time=5, iterations=8): #give it a time interval

    times = np.zeros(iterations)
    halls = np.zeros(iterations)
    init_time = t.time()
    
    for i in range(iterations):
        print("Retreiving value {}...".format(i+1 ))
        halls[i] = get_hall()
        times[i] = t.time()-init_time #time since started the experiment
        print("{:0.2e} [V]    {:0.2f} [s]".format(halls[i], times[i]))
        t.sleep(time)
        
    return halls, times

#Just to set the temperature before doing the experiment
def update_temp():
    thermo = tc.Thermocouple()
    while True:
#        clear()
        print("%0.2f K" %(thermo.toKelvin(get_temp())))
        t.sleep(1)
#        i = input("Enter text (or Enter to quit): ")
#        if not i:
#            break
    return

#Output filename should look like:
#<BFIELD_STRENGHT>_<ANGLE_ON_SAMPLE>_<START_TEMP>.txt
def retreive_all(time=1, iterations=8, filename=None, foldername=None): #give it a time interval
   
    if filename is None:
        print("\nIf B-Field is < 0, start with 'n' instead of '-'!\n")
        print("\nUsual filename: <BFIELD_STRENGHT>_<ANGLE_ON_SAMPLE>_<START_TEMP>\n")
        filename = raw_input("Save to (filename)?:  ")
        filename += ".txt"
    else:
        print("Saving to {}".format(foldername))

#    if foldername is None:
#        #print("\nIf B-Field is < 0, start with 'n' instead of '-'!\n")
#        #print("\nUsual filename: <BFIELD_STRENGHT>_<ANGLE_ON_SAMPLE>_<START_TEMP>\n")
#        foldername = raw_input("\nCreate new folder?:  ")
#        foldername += ".txt"
#    else:
#        print("Creating {}".format(foldername))
#
#    os.mkdir("../database/{}/".format(foldername))


    d = s.data.databox()
    labels = ["v{}".format(i+1) for i in range(8)]
    labels.append("time")
#    for i in range(iterations):
#        d["v{}".format(i+1)] = []
#    print(labels)
    #d['time'] = []
    d.ckeys = labels
    
    #times = []#np.zeros(iterations)
    #voltages = []#np.zeros(iterations)
    init_time = t.time()
    
#    d.h
    
    for i in range(iterations):
        print("\nRetreiving value {}...".format(i+1))
#        voltages[i] = get_allVoltages()
        temp_volts = np.array(get_allVoltages())
        temp_volts = np.append(temp_volts, np.round(t.time()-init_time, decimals=2))
#        for i in range(len(temp_volts)):
#            d['v{}'.format(i+1)].append_data_point(temp_volts[i])
        d.append_data_point(temp_volts)
        #Time might be a problem, since voltages are not measured simultaneously
#        times[i] = t.time()-init_time #time since started the experiment
#        d['time'].append_data_point(t.time()-init_time)
        print(get_hall())
#        print("{:0.2e} [V]    {:0.2f} [s]".format(halls[i], times[i]))
        t.sleep(time) #
#    print(voltages)
#    v1 = voltages[0::8]
#    v2 = voltages[1::8]
#    v3 = voltages[2::8]
#    v4 = voltages[3::8]
#    v5 = voltages[4::8]
#    v6 = voltages[5::8]
#    v7 = voltages[6::8]
#    v8 = voltages[7::8]
#    thermo = tc.Thermocouple
#    temp = np.zeros(np.shape(v8))
#    for i in range(len(v8)):
#        temp[i] = thermo.toKelvin(v8[i])
#    print(v1)
#    voltages = [v1,v2,v3,v4,v5,v6,v7,temp]
#    print(voltages)
#        
#    for i in range(len(voltages)):
#        d.append_column(np.array(voltages[i]), labels[i])
#    d.append_column(times)
    
#    d.save_file("../database/{}/{}".format(foldername,filename))
    d.save_file("../database/{}".format(filename))
        
    return #voltages, times
        
#retreive_all(iterations=1,filename="test")    
#data = s.data.load("../database/test")
#update_temp()
retreive_all()
