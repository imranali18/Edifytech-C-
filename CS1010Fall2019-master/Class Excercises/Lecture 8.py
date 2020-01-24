# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:35:22 2019

@author: mushtu
"""

def isright(a,b,c):
    if ((a**2)+(b**2))==(c**2):
        return True
    else:
        return False

print(isright(3,4,5))
print(isright(3,4,6))



