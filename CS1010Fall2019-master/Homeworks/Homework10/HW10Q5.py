# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:23:15 2019

@author: mushtu
"""

# function to return key for any value 
def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
  
# Driver Code 
  
my_dict ={"java":100, "python":112, "c":11, "R":131} 
  
print(get_key(100)) 
print(get_key(111)) 
