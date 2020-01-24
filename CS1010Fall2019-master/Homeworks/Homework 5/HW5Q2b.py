# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:45:41 2019

@author: mushtu
"""

def Average_add(a):
    l=sum(a)/len(a)
    a.append((l))
    return a

##Test Cases
Average_add ([1,2,3]) 
Average_add ([7,1,4]) 
Average_add ([0,2,10])
