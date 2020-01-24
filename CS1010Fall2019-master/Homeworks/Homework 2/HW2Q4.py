#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 16:06:40 2019

@author: uzma
"""
str1=str(input('Input the string '))
char = str1[0]
str1 = str1.replace(char, '&')
str1 = char + str1[1:]
print(str1)