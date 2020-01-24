# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 08:27:45 2019

@author: mushtu
"""

values=['a','b','c']
for i in range(len(values)):
    print (i, values[i]) 
    










    
    
for i in range(len(values)):
    values[i]='X'
    
values


















values=[1,2,3]
for i in range(len(values)):
    values[i]=2*values[i]  #OR values[i]*=2

values













for pair in enumerate(values):
    i=pair[0] ##index because this is the 1st element of pair
    j=pair[1]  ##Actual value
    values[i]=2*j

values













for (i, v) in enumerate(values):
    values[i] = 2 * v

values














samplestr='Hello World'
# Iterate over the first three elements of string
for elem in samplestr[0:3:1]: 
    print(elem)




for elem in samplestr[::2]:
    print(elem)


for elem in samplestr[ : :-1]:
    print(elem)
    
    
    
    



