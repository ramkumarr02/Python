# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:24:10 2016

This program calculates the distance between two co-ordinates

@author: ramrajagopalan
"""

class Line(object):
    def __init__ (self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def Distance(self):
       return ((abs(self.p2[0]-self.p1[0])**2) + (abs(self.p2[1]-self.p1[1])**2))**0.5
        
    def Slope(self):
        return float(abs(self.p2[1]-self.p1[1]))/float(abs(self.p2[0]-self.p1[0]))


l = Line((3,2),(8,10))

d = l.Distance()
print d

s  = l.Slope()
print s 