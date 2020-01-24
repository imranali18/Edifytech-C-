#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:22:22 2019

@author: uzma
"""

k = 10
if (k == 10): 
    if (k < 15): 
        print ("k is in the first if statement") 
    if (k < 12): 
        print ("k is in the nested if")
    else:
        print ("k is in the else block of nested if") 
##Nested if

k = 10
if (k == 10): 
    #  First if statement 
    if (k < 15): 
        print ("k is is in first if statement") 
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (k < 12): 
        print ("k is in the nested if") 
    else: 
        print ("k is in else block of nested if") 
        








        
        
l = 20
if (l == 10): 
    print ("l is 10") 
elif (l == 15): 
    print ("l is 15") 
elif (l == 20): 
    print ("l is 20") 
else: 
    print ("l is not present") 
        
 











#Boolean Algebra (AND)
x=True
y=True
x and False == False
#False and x ==False  
y and x == x and y
x and True == x
True and x == x
x and x == x   







##Boolean Algebra (OR)
x=True
y=False
x or False == x
False or x == x
y or x == x or y
x or True == True
True or x == True
x or x == x  

#NOT Operator
not (not x) == x   
not x == x









#Demorgan's law (Boolean variables)
x=True
y=False
not (x and y) == (not x) or (not y)
not(x or y) == (not x)and(not y)















##Typecasting
int('12')
int('Hello') ##Must error out
int(15.2)
int(-2)
float('1.4')
float(5.9)
float(5)
str('20')
str(25)
str('abcdef')















##Floaing Point Numbers
import math
a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)

##One way of dealing with this issue
print(math.floor(a*a)==2.0)












