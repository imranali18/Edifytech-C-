#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:12:44 2019

@author: uzma
"""

##Addition
print(2+1)
print(3+2)
print(8+3)
##Substraction
print(5-4)
#Multiplication
print(3*5)
#Division
print(7/2)
print(8/3)
#Floor Division (Truncates the decimal without rounding)
print(7//2)
print(8//3)
##Modulo (Only the remainder)
print(7%2)
##Powers
print(2**3)
#Order of Operations: PEMDAS
print(2 + 10 * 10 + 3)
# Can use parentheses to specify orders
print((2+10) * (10+3))

#Variable Assignment
##Create an object called a and assign it value 
a=5
print(a)
##Add objects
print(a+a)
##Let's try re-assignment
a=20
print(a)
print(a+a)
# Use A to redefine A
a = a + a
print(a)

# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate

print(my_taxes)

print('My Taxes are', my_taxes)

##Dynamic typing
b=10
b=['new']
print(b)

#Re-assignment
a=5
a+=5
print(a)

a*=5
print(a)

#Check variable type
type(a)
type(my_taxes)
 ##User input
print('Input your age')
b=input()
a=input()
print("Age is",b)

##Operaters
a==b
a!=b

##Chained Operators
#Implicit and
1<2<3

1<3>2

1<5>6

#Explicit And
1<2 and 4<3

#OR Condition

1==2 or 1<3

##Test Keywords
print (None == 0) 
print(not True)

