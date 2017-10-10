# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import keithley
import time as t
import numpy as np

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
        print("Retreiving value {}...".format(i+1))
        halls[i] = get_hall()
        times[i] = t.time()-init_time #time since started the experiment
        print("{:0.2e} [V]    {:0.2f} [s]".format(halls[i], times[i]))
        t.sleep(time)
        
    return halls, times

def retreive_all(time=1, iterations=8): #give it a time interval

    times = np.zeros(iterations)
    voltages = np.zeros(iterations)
    init_time = t.time()
    
    for i in range(iterations):
        print("Retreiving value {}...".format(i+1))
        voltages[i] = get_allVoltages()
        times[i] = t.time()-init_time #time since started the experiment
#        print("{:0.2e} [V]    {:0.2f} [s]".format(halls[i], times[i]))
        t.sleep(time) #
    
    v1 = 
        
    return voltages, times
        
halls, times = retreive_hall()    