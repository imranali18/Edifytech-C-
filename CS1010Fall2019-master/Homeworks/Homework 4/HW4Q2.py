#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:02:50 2019

@author: uzma
"""

def near_ten(num):
  m=num % 10
  return ((m>=0 and m<=2) or (m>=8))


