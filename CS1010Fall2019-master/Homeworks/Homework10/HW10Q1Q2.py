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


##Q2
squares = {1:1, 2:4, 3:9, 4:16, 5:25} 
del squares[4]
squares


squares[6]=36
squares
