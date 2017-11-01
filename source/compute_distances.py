#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:33:00 2017

@author: felix
"""
import numpy as np

def compute_distance(caliper1, caliper2, farpoint1, farpoint2, closepoint1, closepoint2):

    mm0p25 = caliper2-caliper1
    
    fardistance = farpoint2 - farpoint1
    closedistance = closepoint2 - closepoint1
    
    real_farDistance = 0.25*fardistance/mm0p25
    real_closeDistance = 0.25*closedistance/mm0p25 
    
    mean_distance = np.mean([real_closeDistance, real_farDistance])
    mean_error = (real_farDistance - real_closeDistance)/2
    
    print("Distance: {} +/- {}".format(mean_distance, mean_error))
    
    return mean_distance, mean_error

v5_distance = compute_distance(325.795, 343.303, 182.660, 539.977, 220.267, 495.476)
v6_distance = compute_distance(391.725, 407.272, 244.076, 557.528, 292.244, 536.679)

l_sample = [9.48, 0.02]
d_sample = [1.01, 0.02]
w_sample = [2.70, 0.02]

np.save("../database/distance_v5", v5_distance)
np.save("../database/distance_v6", v6_distance)
np.save("../database/l_sample", l_sample)
np.save("../database/d_sample", d_sample)
np.save("../database/w_sample", w_sample)