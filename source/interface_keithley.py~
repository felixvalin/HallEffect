# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""Don't Forget to GIT PULL before doing anything !!!"""

#git pull origin master

#git add -A && git commit -a -m "new update of Hall Angle" && git push origin master


import keithley
import time as t
import numpy as np
import spinmob as s
import thermocouple as tc
import os
import matplotlib.pyplot as plt

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
    plt.figure()
    plt.xlabel("Time [s]")
    plt.ylabel("Temperature [K]")
    i = 0
    try:
        while True:
    #        clear()
            temp = np.float(thermo.toKelvin(get_temp()))
            print("{0:0.2f} K".format(temp))
            plt.plot(i, temp, 'b+')
            plt.pause(1)
            i+=1
    #        i = input("Enter text (or Enter to quit): ")
    #        if not i:
    #            break
    except KeyboardInterrupt:
        pass
    
    return

#Output filename should look like:
#<BFIELD_STRENGHT>_<ANGLE_ON_SAMPLE>_<START_TEMP>.txt
def retreive_all(time=1, iterations=0, sleep= False, filename=None, foldername=None): #give it a time interval
   
    if filename is None:
        print("\nIf B-Field is < 0, start with 'n' instead of '-'!\n")
        filename = raw_input("Save to (filename)?:  ")
        filename += ".txt"
    else:
        filename += ".txt"
        print("Saving to {}".format(filename))

    if foldername is None:
        #print("\nIf B-Field is < 0, start with 'n' instead of '-'!\n")
        #print("\nUsual filename: <BFIELD_STRENGHT>_<ANGLE_ON_SAMPLE>_<START_TEMP>\n")
        foldername = raw_input("\nNew folder name?:  ")
    else:
        print("\nCreating folder {}".format(foldername))

    try:
        os.mkdir("../database/{}/".format(foldername))
    except OSError:
        print("Folder already exists! Continuing...")
        pass

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
    if iterations == 0:
        i=0#For the counter to work!
        plt.figure()
        plt.xlabel("Time [s]")
        plt.ylabel("Temperature [K]")
        
        previous_temperature = 0
        previous_time = 0
        
        try:
            while True:
                print("\nRetreiving value {}...".format(i+1))
        #        voltages[i] = get_allVoltages()
                temp_volts = np.array(get_allVoltages())
                time = t.time()-init_time
                temp_volts = np.append(temp_volts, np.round(time, decimals=2))
                thermo = tc.Thermocouple()
                temperature = np.float(thermo.toKelvin(temp_volts[7]))
                plt.plot(time, temperature, 'b+')
                print("SLOPE: {0:0.3f} K/s".format((temperature-previous_temperature)/(time - previous_time)))
                print("TEMPERATURE: {0:0.2f} K".format(temperature))
        #        for i in range(len(temp_volts)):
        #            d['v{}'.format(i+1)].append_data_point(temp_volts[i])
                d.append_data_point(temp_volts)
                previous_temperature = temperature
                previous_time = time
                plt.pause(1)
                
                #Time might be a problem, since voltages are not measured simultaneously
        #        times[i] = t.time()-init_time #time since started the experiment
        #        d['time'].append_data_point(t.time()-init_time)
    #            print(get_hall())
        #        print("{:0.2e} [V]    {:0.2f} [s]".format(halls[i], times[i]))
                if sleep:
                    if i>100:
                        t.sleep(time) #This creates a pause in the loop after a few iterations
                if temperature>=380:#This stops the loop if we exceed a given temperature
                    print("Exceeded maximal temperature!\nMax Temp: {0:0.2f} K\nCurrent Temp: {1:0.2f} K".format(380, temperature))
                    break
#                if temp_volts[-1] > 7200:
                if temp_volts[-1] > 14400:
#                    print("Exceeded maximal run time (2hr)!. Stopping...")
                    print("Exceeded maximal run time (4hr)!. Stopping...")
                    break
                i+=1#For counting measures
        #This interrupts data taking and goes to save the file automatically
        #instead of crashing
        
        #USAGE: Ctrl-C
        except KeyboardInterrupt:
            print("Terminating...")
            pass
    else:
        for i in range(iterations):
            print("\nRetreiving value {}...".format(i+1))
    #        voltages[i] = get_allVoltages()
    #        voltages[i] = get_allVoltages()        except KeyboardInterrupt:
            print("Terminating...")
            pass
            temp_volts = np.array(get_allVoltages())
            temp_volts = np.append(temp_volts, np.round(t.time()-init_time, decimals=2))
            thermo = tc.Thermocouple()
            print("TEMPERATURE: {} K".format(thermo.toKelvin(temp_volts[7])))
    #        for i in range(len(temp_volts)):
    #            d['v{}'.format(i+1)].append_data_point(temp_volts[i])
            d.append_data_point(temp_volts)
            #Time might be a problem, since voltages are not measured simultaneously
    #        times[i] = t.time()-init_time #time since started the experiment
    #        d['time'].append_data_point(t.time()-init_time)
            print(get_hall())
    #        print("{:0.2e} [V]    {:0.2f} [s]".format(halls[i], times[i]))
#            if sleep:
#                if i<20
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
#        foldername
#    for i in range(len(voltages)):
#        d.append_column(np.array(voltages[i]), labels[i])
#    d.append_column(times)
    
    print("Saving file to ../database/{}/{}".format(foldername,filename))    
    d.save_file("../database/{}/{}".format(foldername,filename))
    #d.save_file("../database/{}".format(filename))
        
    return #voltages, times

def voltage_input():
    try:
        v = np.float(raw_input("\nWhat is the voltage reading (in [V])?: "))
#        v = np.float(input("What is the voltage reading (in [V])?: "))
    except ValueError:
        print("\nYou must enter a valid voltage reading!")
        v = voltage_input()
    
    return v

def mr():
    
#    volt = [0.174,0.128,0.092,0.051,0.013]
#    angles = np.linspace(0,320, 9)
#    volt = [1]
#    angles = [1]
    angles = [296, 116]
    
    d = s.data.databox()
    labels = ["v{}".format(i+1) for i in range(8)]
    labels.append("volt")
#    labels.append("angle")
    d.ckeys = labels
    
    try:
        for a in angles:
            print("\nMake sure angle 240 [deg] (on the tube)\nis pointing at you before you start!\n")
            print("Set angle to {} [deg]".format(a,a))
            raw_input("Press enter whenever you're ready...")
#            input("Press enter whenever you're ready...")
            while True:
                print("\nChange the B-Field:\n-->Set DMM to Front\n-->Turn off DMM\n-->Plug Hall Probe in USB\n-->Turn DMM on\n-->Measure B-Field")

                v = voltage_input()
                
                if a == 116:
                    v *= -1
                print("\n-->Turn off DMM\n-->Set DMM to rear\n-->Done!")
                raw_input("Press enter whenever you're ready...")
#                input("Press enter whenever you're ready...")
                dmm = keithley.DMM()
                ########TEST#########
#                print("")
#                print("Found DMM")
                #####################
                print("\nMeasuring voltages...\n")
                for i in range(5):
                    print("{}: ".format(i))
                    results = np.array(get_allVoltages())
#                    results = np.zeros(8)
#                    for j in range(8):
#                        results[j] = j
                    results = np.append(results, [v])
                    d.append_data_point(results)
                    print(results)
                    print("")
                
                answer = raw_input("Continue with angle {}? [y/n]: ".format(a))
#                answer = input("Continue with angle {}? [y/n]: ".format(a))
                if answer == "n":
                    break
                    
                
    except KeyboardInterrupt:
        print("Terminating...")
        pass
            
    foldername = raw_input("Foldername? ")
#    foldername = input("Foldername? ")    
        
    try:
        os.mkdir("../database/{}/".format(foldername))
    except OSError:
        print("Folder already exists!")
        pass

    print("Saving file to ../database/{}/magneto_resistance.txt".format(foldername))
        
    d.save_file("../database/{}/magneto_resistance.txt".format(foldername))

        
def magneto_resistance():

    volt = [0.174,0.128,0.092,0.051,0.013]
    angles = np.linspace(0,320, 9)
#    volt = [1]
#    angles = [1]
    
    d = s.data.databox()
    labels = ["v{}".format(i+1) for i in range(8)]
    labels.append("volt")
    labels.append("angle")
    d.ckeys = labels
    
    try:
        for v in volt:
            print("Set volt to {} [V]".format(v))
            raw_input("Press enter...")
            dmm= keithley.DMM()
            for a in angles:
                print("Set angle to {} [deg]".format(a))
                raw_input("Press enter...")
                for i in range(3):
                    print("{}: \n".format(i))
                    results = np.array(get_allVoltages())
                    results = np.append(results, [a, v])
                    d.append_data_point(results)
                    print(results)
                    
                
    except KeyboardInterrupt:
        print("Terminating...")
        pass
            
    foldername = raw_input("Foldername? ")
            
    try:
        os.mkdir("../database/{}/".format(foldername))
    except OSError:
        print("Folder already exists! Continuing...")
        pass

    print("Saving file to ../database/{}/magneto_resistance".format(foldername))
    d.save_file("../database/{}/magneto_resistance".format(foldername))

        
    d.save_file("../database/{}/magneto_resistance.txt".format(foldername))

#retreive_all(iterations=1,filename="test")    
#data = s.data.load("../database/test")
#update_temp()
#datasets = np.linspace(0,360,19)
#
#for angle in datasets:
#    angle = np.int(angle)
#    filename = "{}_hall_angle".format(angle)
#    print("\n-------------------------------------------\n")
#    print("Make sure the apparatus is setup at {} [deg]".format(angle))
#    raw_input("Press Enter to continue")
#    retreive_all(filename=filename)
##    print("\n-------------------------------------------\n")

#For cool to hot!
#retreive_all(iterations=0)
#update_temp()
#retreive_all(iterations=0, foldername="nitrogenRun_261017")
#retreive_all(time=4, iterations=0, sleep=True, foldername="Nitrogen_Run_191017_1")
