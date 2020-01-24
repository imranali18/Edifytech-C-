#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 18:19:27 2019

@author: uzma
"""

##Problem 2 Lecture 7
3==3
3!=3
3>=4
not(3<4)











##Problem 3
def isright(a,b,c):
    return (a^2+b^2 ==c^2)

isright(2,3,4)
isright(3,4,5)


















##Problem 4
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars>=40
  else:
    return (cigars>=40 and cigars<=60)


cigar_party(30, True)
cigar_party(90, True)
cigar_party(80, False)
















##Problem 5
def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum

sorta_sum(9,4)
sorta_sum(10,12)











