# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:56:46 2019

@author: mushtu
"""

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 
