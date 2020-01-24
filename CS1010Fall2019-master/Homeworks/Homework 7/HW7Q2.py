# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:52:34 2019

@author: mushtu
"""

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


print(perfect_number(28))
