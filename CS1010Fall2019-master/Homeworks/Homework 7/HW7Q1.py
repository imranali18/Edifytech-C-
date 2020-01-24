# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:31:31 2019

@author: mushtu
"""

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
s = ''
for i in q:
    for j in range(len(i)):
        s = s + i[j]
print(s)