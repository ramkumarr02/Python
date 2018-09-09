# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 00:16:17 2016

@author: ramrajagopalan

"""
# Added to Git Hub

class Cylinder(object):
    pi = 3.14
    
    def __init__(self,h,r):
        self.h = h
        self.r = r
        print "Cylinder Created"
        
    def volume(self):
        return self.pi * self.r**2 * self.h
    
    def surface_area(self):
        return (2 * self.pi * self.r * self.h) + 2 * self.pi * self.r**2
        
cyl = Cylinder(2,3)

print cyl.volume()
print cyl.surface_area()