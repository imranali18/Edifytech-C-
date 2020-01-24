# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:50:46 2019

@author: mushtu
"""

import math
def circle(radius):
    """ Compute and return the area of a circle """
    return math.pi * radius**2


def cylinder(radius,height):
    """ Compute and return the surface area of a cylinder """
    circle_area = circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2 * circle_area + height_area


def sphere(radius):
    """ Compute and return the surface area of a sphere """
    return 4 * math.pi * radius**2




