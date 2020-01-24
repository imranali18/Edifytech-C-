# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:02:35 2019

@author: mushtu
"""

"Rensselaer"
s='Rensselaer'
print(s)
'4 5 67 8'
'   '
type('xyz')
str(5)
#Functions in strings
len(s)
t='He said, "Hello World"'
print(t)
s1="C''''''''mon"
print(s1)

t= """This extends in
multiple lines"""

#Escape characters \
t= "This extends in \n multiple lines"
print(t)
u='column1\tcolumn2\tcolumn3'
print(u)
print('You can \\ do this')
print('\\')
##Accessing the elements: Indexing
s[0]
s[2]
s[9]
s[len(s)-1]
s[-1]
#Slicing [begin:stop:step]
s='Rensselaer'
s[1:5]
s
#Concatenation
'Hello '+'World'+'!'
s1='Hello'
s2='World'
s1+s2
'Hello''World'
print(s1+s2)
#Replication
'lol'*10
##Methods: variable.method(argument)
s='Good Morning'
s.find('o',3)
s.replace('o','@')
s
#More methods on output
t='Uzma Mushtaque'
t=t.lower()
t
t.upper()
t.title()
t.capitalize()
t.count('m','M')
##Print formatting
print('The value of variable'+'13'+'')
#.format method
x=12/11
y=13/7
print('The value of y is {0:.2f} and x is {1:.2f}'.format(x,y))





























