# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:19:44 2019

@author: mushtu
"""

#Problem 1
#Create a set 
num_set = set([0, 1, 2, 2, 3, 4, 4, 5])
for n in num_set:
    print(n)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Problem 2
#A new empty set
color_set = set()
color_set.add("Red")
print(color_set)
#Add multiple items
color_set.update(["Blue", "Green"])
print(color_set)





















#Problem 3
#Remove common elements
set_x = set(["apple", "mango"])
set_y = set(["mango", "orange"])
#Symmetric difference
set_c = set_x ^ set_y
print(set_c)


















#Problem 4
A={1, 3, 5}
B={3, 5, 6}
A&B
A|B
#LHS is not equal to RHS









