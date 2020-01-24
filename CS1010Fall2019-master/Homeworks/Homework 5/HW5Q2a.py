# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:41:59 2019

@author: mushtu
"""

def Tens_swap(a): 
    l1=a[0]//10
    l2=a[-1]//10
    if l1==l2:
        return True
    return False

##Test Cases
Tens_swap((21,12,45,67,29))
Tens_swap((32, 45,23)) 
Tens_swap((76,89,23,45,10,70)) 
