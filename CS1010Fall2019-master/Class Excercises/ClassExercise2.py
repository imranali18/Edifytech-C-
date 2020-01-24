#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 17:22:53 2019

@author: uzma
"""
##Question 1
A = str(input("Input the string"))
X=A[0]
Y=A[-1]
Z=A[1:-1]
print(Y + Z + X)

##Question 2
B=str(input('Enter the string '))
x=B[0]
if x in B[1:]:
    print('True')
else:
    print('False')
    
##Question 3
str1=str(input("Input first string"))
str2=str(input("Input second string"))
if len(str1)!=len(str2):
    if len(str1)>len(str2):
        print(str1.replace(str2[-1],'$'))
    else:
        print(str2.replace(str1[-1],'$'))
else:
    print('Both are equal')
    
    
