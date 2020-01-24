#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 13:12:18 2019

@author: uzma
"""

# A simple Python function to check 
# whether x is even or odd 
def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")
 




       
        
##Max of two numbers
def max_of_two( x, y ):
    if x > y:
        return x
    return y

max_of_two (12,14)



##Max of 3 numbers
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )

##Call the function
print(max_of_three(3, 6, -5))





##function that checks if a number is in a given range or not

def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')