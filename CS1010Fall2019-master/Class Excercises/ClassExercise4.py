#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:59:51 2019

@author: uzma
"""

##Problem 1
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a>=b:
            return b
        else:
            return a    
    else:
        if a>=b:
            return a
        else:
            return b










        
##Although this code works just fine we can refine it
##Use built in min max functions
def lesser_of_two_evens1(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
        
        
 











#Problem 2
def wordmapping(word1,word2):
##Lets try to get rid of if statements as much as possible
    return word1[0]!=word2[0]

##Call the function
wordmapping('Chair','Car')   
wordmapping('Table','Car') 

















##Problem 3

def namecap(name):
    if len(str(name)) >= 5:
        return name[0]+name[1].capitalize()+name[2:4]+name[4].capitalize()+name[5:]
    else:
        return 'Name is too short!'















#Problem 4
import math
def calc(num):
    print('Factorial is ', math.factorial(int(num)))
    print('Floor is ', math.floor(num))
    print('Ceiling is ', math.ceil(num))
    print('Exponential is ', math.exp(num))

##Call
calc(6.76)
math.pi





















#Problem 5
import math

def calc_circle(radius):
    return math.pi * radius ** 2


def calc_cone(radius,height):
    circle_area = calc_circle(radius)
    return (1/3*(circle_area*height))

print('The area of a circle of radius 2 is', calc_circle(2))
print('The volume of a cone of radius 2 and height 5 is', calc_cone(2,5))


















##Solution to class excercise
def vend_mc_validate(n1,n2):
    return (n1+n2)==10 or (n1+n2)==20 or (n1+n2)==50 or n1==10 or n2==10 or n1==20 or n2==20 or n1==50 or n2==50


