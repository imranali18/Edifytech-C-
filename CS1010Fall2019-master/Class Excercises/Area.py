# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:24:05 2019

@author: mushtu
"""

import math
#Area of a circle
def circle(radius):
    return math.pi * radius**2

#Area of cylinder
def cylinder(radius,height):
    circle_area = circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2 * circle_area + height_area

#Area of sphere
def sphere(radius):
    return 4 * math.pi * radius**2

#Area of cone
def cone(radius, height):
    slant_area=math.pi*radius*(math.sqrt(height^2+radius^2))
    return circle(radius)+slant_area



