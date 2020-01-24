#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:02:57 2019

@author: uzma
"""
##Define our first function
def getGroceries():
    print('milk')
    print('flour')
    print('sugar')
    print('butter')
    print()   #blank line
    
# Main code starts here
getGroceries()













##Modify
def getGroceries(item1):    # uses one parameter variable
    print(item1)  # prints the contents of the item1 variable
    print('flour')
    print('sugar')
    print('butter')
    print()
 
    
    
    
    
    
    
    
    
    
    
#Make it more generic
def getGroceries(item1, item2, item3, item4):
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    print()
 
    
 
    
    
    
    
    
    
    
##Main code
# Now call the function with four arguments
getGroceries('eggs', 'soap', 'lettuce','cat food')
getGroceries('beer', 'milk', 'soda', 'peas')








##Addition function
def addTwo(startingValue):
    endingValue = startingValue + 2
    print('The sum of', startingValue, 'and 2 is:', endingValue)




# Call the function twice with different arguments
addTwo(5)
addTwo(10)











##One more built in function
##Range function        
3 in range(0,5)
l=range(1,4) ##4 not included
4 in l
3 in l



##Keywords

##Function to add two numbers
##Introducing keyword return
def sum_two_numbers(a, b):
    return a + b

##Keyword argv in python
def myFun(*argv):   
        print (argv) 


        
 






       
##Math class
import math

math.floor(15.25)
math.factorial(5)
math.exp(2)



##Strings class
import string
s='Apple'
s.lower()
s.capitalize()
s.upper()



##All letters of the alphabet
string.ascii_uppercase
string.ascii_lowercase
string.ascii_letters




