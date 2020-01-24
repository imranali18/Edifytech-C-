#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:54:23 2019

@author: uzma
"""

num=int(input('Enter the number '))
if num%3==0 and num%5==0:
    print('YES')
elif num%3==0 or num%5==0:
    print('NO')
else:
    print('UNKNOWN')