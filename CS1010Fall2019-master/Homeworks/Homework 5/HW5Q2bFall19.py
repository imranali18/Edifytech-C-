# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:35:43 2019

@author: mushtu
"""
import math
def find_dist(a,b):
    return round(math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2))

print(find_dist((2,3),(5,7)))
print(find_dist((6,-3),(-4,7)))
