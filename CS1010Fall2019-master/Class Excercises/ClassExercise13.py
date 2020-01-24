# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:59:11 2019

@author: mushtu
"""


# Python program to handle simple runtime error 
  
a = [1, 2, 3] 
try:  
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3]) ) 
  
except IndexError: 
    print ("An error occurred")







# Program to handle multiple errors with one except statement 
try :  
    a = 3
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print ("Value of b = ", b )
  
# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
    print ("\nError Occurred and Handled")
    
    
    
    
    
    
    
    
    

# Program to depict else clause with try-except 
  
# Function which returns a/b 
def AbyB(a , b): 
    try: 
        c = ((a+b) / (a-b)) 
    except ZeroDivisionError: 
        print ("a/b result in 0")
    else: 
        print (c)
  
# Driver program to test above function 
AbyB(2.0, 3.0) 
AbyB(3.0, 3.0) 






#Problem 4
def capitalize_list(names):
    cap_names = []
    for n in names:
        cap_names.append(n.capitalize())
    names = cap_names
    
animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
capitalize_list(animals)
print(animals)




















def capitalize_list(names):
    for n in names:
        n = n.capitalize()
        
animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
capitalize_list(animals)
print(animals)
        
 














       
def capitalize_list(names):
    i = 0
    while i < len(names):
        names[i] = names[i].capitalize()
        i += 1
        
animals = ['cat', 'monkey', 'hawk', 'tiger', 'parrot']
capitalize_list(animals)
print(animals)






















## problem 5
l1=[320.03, 322.16, 328.07, 333.91, 341.47,  348.92, 357.29, 363.77, 371.51, 382.47, 392.95]
sum1=0
for i in l1:
    sum1=sum1+i
print(sum1/len(l1))











