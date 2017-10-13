# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:33:14 2016

@author: mark.orchard-webb
"""

import time
import thermocouple
import numpy
import spinmob as s

class Hall:
    def __init__(self,filename=None):
        if None == filename:
            raise IOError("A file name must be supplied");
        d = s.data.load()
        voltages = [v for v in d]
#        fh = open(filename,"r");
#        mode = 0;
#        headcount = 0;
#        linecount = 0;
#        v = [[],[],[],[],[],[],[],[]];
#        clock = []
#        while 2 != mode:
#            line = fh.readline(512);
#            linecount = linecount + 1;
#            if 0 == mode:
#                if "%" == line[0]:
#                    headcount = headcount + 1;
#                else:
#                    if 22 != headcount:
#                        print("parsed %d lines of header, was expecting 22" % (headcount))
#                    mode = 1;
#            if 1 == mode:
#                if None == line or 0 == len(line):
#                    print()
#                    mode = 2
#                else:
#                    line = line.replace("\n","");
#                    line = line.replace("\t"," ");
#                    line = line.replace("  "," ");
#                    words = line.split(" ");
#                    if 9 != len(words):
#                        errstr = "At line %d of data %d words were found (line = '%s'" % (linecount,len(words),line)
#                        raise IOError(errstr)
#                    for i in range(8):
#                        v[i].append(float(words[i]))
#                        clock.append(int(words[8]))
#        print "read %d lines from %s, data spans %s starting at %s" % (linecount,filename,self.interval(clock[0],clock[len(clock)-1]),self.timestamp(clock[0]))
#        self.v1 = numpy.array(v[0]);
#        self.v2 = numpy.array(v[1]);
#        self.v5 = numpy.array(v[4]);
#        self.v6 = numpy.array(v[5]);
#        typeT = thermocouple.Thermocouple('T');
#        self.T = typeT.toKelvin(numpy.array(v[7]));
    def interval(self,start,stop):
        delta = stop - start;
        if 0 == delta:
            return "0 seconds";
        if delta < 300:
            return "%d seconds" % (delta);
        if delta < 3600:
            min = delta / 60;
            return "%d minutes, %d seconds" % (min, delta-60*min);
        hr = delta / 3600;
        min = (delta - 3600*hr) / 60;
        return "%d hours, %d minutes" % (hr, min)
    def timestamp(self,start):
        tm = time.localtime(start);
        return time.strftime("%Hh%M on %A %B %d, %Y",tm)