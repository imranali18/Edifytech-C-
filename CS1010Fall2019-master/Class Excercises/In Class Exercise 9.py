# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:28:52 2019

@author: mushtu
"""

f=open('One.txt','r')
One = f.read()
f.close()

g=open('Two.txt','r')
Two = g.read()
g.close()


One = One.split("\n")
type(One)
print(One)
One = set(One)
One


Two = Two.split("\n")
type(Two)
print(Two)
Two = set(Two)
Two

##Part a intersection
Common=One & Two
#len(Common)
print(Common)

##Part b length of union
New=(One|Two)
len(New)

##Part c symmetric diffrence
Notinboth = One ^ Two
len(Notinboth)
