# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:26:41 2019

@author: mushtu
"""
#Problem 1
def first_last6(x):
    if x[0]==6 or x[-1]==6:
        return True
    return False

print(first_last6([6,2,8]))

#Problem 2
def common_end(x,y):
    if x[0]==y[0] or x[-1]==y[-1]:
        return True
    return False

print(common_end([6,2,8],[1,8]))

#Problem 3
def big_diff(x):
    x=sorted(x)
    return x[-1]-x[0]

print(big_diff([6,0,3,10]))

#Problem 4
def rotate_left3(x):
    a=x[0]
    b=x[1]
    c=x[2]
    return [b,c,a]

print(rotate_left3([3,4,5]))





