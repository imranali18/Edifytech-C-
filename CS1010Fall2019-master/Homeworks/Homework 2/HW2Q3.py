#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:48:02 2019

@author: uzma
"""
str1=str(input('Enter the string'))
length = len(str1)
if length > 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
    else:
        str1 += 'ing'
print(str1)