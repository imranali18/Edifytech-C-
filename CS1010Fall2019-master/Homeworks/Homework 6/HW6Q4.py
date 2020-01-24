# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:01:25 2019

@author: mushtu
"""

# take input from the user
num1 = int(input("Enter the upper range: "))
num2 = int(input("Enter the lower range: "))

i=num2
while i in range(num2,num1+1):
    if i%2!=0:
        print(i)
    i+=1
print()