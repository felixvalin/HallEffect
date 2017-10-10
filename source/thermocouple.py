# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:55:29 2016

@author: mark.orchard-webb
"""

import scipy
from scipy.interpolate import interp1d

class Thermocouple:
    def __init__(self,type='T'):
        if type == 'T':
            kelvin = scipy.linspace(-270,400,68,endpoint=True) + 273.25;
            voltage = 1e-3*scipy.array([
            -6.258,-6.232,-6.181,-6.105,-6.007,-5.889,-5.753,
            -5.603,-5.439,-5.261,-5.069,-4.865,-4.648,-4.491,-4.177,-3.923,-3.656,
            -3.378,-3.089,-2.788,-2.475,-2.152,-1.819,-1.475,-1.121,-0.757,-0.383,
            0,0.391,0.789,1.196,1.611,2.035,2.467,2.908,3.357,3.813,
            4.277,4.749,5.227,5.712,6.204,6.702,7.207,7.718,8.235,8.757,
            9.286,9.82,10.36,10.905,11.456,12.011,12.572,13.137,13.707,14.281,
            14.86,15.443,16.03,16.621,17.217,17.816,18.42,19.027,19.638,20.252,20.869]);
        else:
            print "There is no data for requested type";
            raise NotImplementedError
        self.interpolation = interp1d(voltage,kelvin,kind='cubic');
    def toKelvin(self,voltage):
        return self.interpolation(voltage);