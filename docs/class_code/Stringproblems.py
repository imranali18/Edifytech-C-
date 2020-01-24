# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:25:00 2019

@author: mushtu
"""

#Problem 1
#Method1
s='I am at work'
s=s.replace('k','@')
s=s.replace('I','k')
s=s.replace('@','I')
#Method 2
s='I am at work'
print(s[-1]+s[1:-1]+s[0])
#Problem 2
B='Hello World'
x=B[0]
if x in B[1:]:
    print('True')
else:
    print('False')
    
#Problem 3
str1=str(input("Input first string"))
str2=str(input("Input second string"))
if len(str1)!=len(str2):
    if len(str1)>len(str2):
        print(str1.replace(str2[-1],'$'))
    else:
        print(str2.replace(str1[-1],'$'))
else:
    print('Both are equal')



















