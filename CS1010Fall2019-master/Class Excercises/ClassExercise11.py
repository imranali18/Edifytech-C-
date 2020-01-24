# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:37:00 2019

@author: mushtu
"""


samplestr='Hello World'
# Iterate over the first three elements of string
for elem in samplestr[0:3:1]: 
    print(elem)














    
def factorial(x):
    count=1
    for i in range(x):
        count=count*(i+1)
    return count
    
factorial(5)    
  















  
def count(sequence,item):
    total=0
    for x in sequence:
        if x==item:
            total+=1
    return total    

count([1,2,3,3,5],3)
















n=5 
for i in range(n): 
    for j in range(i): 
         print ('* ', end="") 
    print('') 

for i in range(n,0,-1): 
    for j in range(i): 
         print('* ', end="") 
    print('') 
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
##Fibonacci series
fib=[0,1]
n=50
for i in range(2,n+1):
    x=fib[i-1]+fib[i-2]
    fib.append(x)    
print(fib)

























# 10 is the total number to print
for num in range(10):
    for i in range(num):
        print (num, end="") #print number
        # new line after each row to display pattern correctly
    print("")











    