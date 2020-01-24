#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:44:53 2019

@author: uzma
"""
##Probalem A
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)
    str1 = str1.replace(' ','')
    return alphaset <= set(str1.lower())  

ispangram('The uick brown fox jumps over the lazy dog')


##Problem B
import math

def calc_circle(radius):
    return math.pi * radius ** 2

def calc_cylinder(radius,height):
    circle_area = calc_circle(radius)
    return (2*circle_area+ math.pi*radius*height)

print('The area of a circle of radius 2 is', calc_circle(2))
print('The surface area of a cylinder of radius 2 and height 5 is', calc_cylinder(2,5))

