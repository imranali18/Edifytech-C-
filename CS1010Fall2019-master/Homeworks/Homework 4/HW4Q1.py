#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 17:48:32 2019

@author: uzma
"""

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <=65:
      return 0
    elif speed>=66 and speed<=85:
      return 1
    else:
      return 2
  else:
    if speed <=60:
      return 0
    elif 61<=speed and speed<=80:
      return 1
    else:
      return 2
