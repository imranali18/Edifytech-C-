#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 10:21:20 2019

@author: uzma
"""


def make_chocolate(small, big, goal):
  if goal>=(5*big):
    if (goal-(5*big)) < small:
      return (goal-(5*big))
    elif (goal-(5*big)) == small:
      return small
    else:
      return -1
  else:
    if goal%5 > small:
      return -1
    else:
      return goal%5
  
    
##Alternate solution
def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - 5 * big
    else:
        remainder = goal % 5
    if remainder <= small:
        return remainder
    return -1