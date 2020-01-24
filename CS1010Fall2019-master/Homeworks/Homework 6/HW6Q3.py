# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:48:45 2019

@author: mushtu
"""

def odd_even_print(n,flag):
    i=0
    if flag==False:
        while i<n:
            i+=1
            if i%2==0:
                continue
            print(i)
    else:
        while i<n:
            i+=1
            if i%2!=0:
                continue
            print(i)
                
        
odd_even_print(13,False)
