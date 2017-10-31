#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:53:01 2017

@author: antoine.neidecker
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:11:47 2016

@author: mark.orchard-webb
"""

import hall
import matplotlib.pyplot as p

h = hall.Hall("cool-nofield");

# This is good for sanity.  Voltages around a closed loop should be zero.
#p.plot(h.T, h.v5+h.v2-h.v6-h.v1)

# This should be a constant 
#p.plot(h.T,h.v5/h.v6)

# This is interesting for determining the amount of leakage of resistivity into "Hall Voltage" meters
# when looking at no-field data --- could potentially perform experiment by measuring ratio of leakage
# from no-field data, then subtract that fraction from a single data set with field rather than using the
# reverse field trick.
#p.plot(h.T,h.v2/h.v5)
#p.plot(h.T,h.v1/h.v5)
#p.plot(h.T,h.v2/h.v6)
#p.plot(h.T,h.v1/h.v6)

# sure enough there is an exponential component to the conductivity
p.semilogy(h.T,1/h.v5)
p.semilogy(h.T,1/h.v6)
p.show()