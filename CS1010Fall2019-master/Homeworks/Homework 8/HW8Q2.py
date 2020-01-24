# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:51:40 2019

@author: mushtu
"""

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("Can't divide by Zero!")
finally:
    print('All Done!')