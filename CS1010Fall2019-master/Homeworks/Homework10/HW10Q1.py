# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:01:42 2019

@author: mushtu
"""

def f1(n):
    n=int(n)
    d = dict()
    for x in range(1,n+1):
        d[x]=x*x
    return(d) 
    
f1(5)
