#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:01:58 2019

@author: uzma
"""
#Scope of variables
y = 20
def printingnum():
    y = 30
    return y


##Print y or call the function
print(y)
print(printingnum())












##Local variables
## x is local here: Cannot be called outside the function
def demmoname():
    x='Uzma'
    return x
    #print('My name is ', x)
    
    
demmoname()












##Enclosing functions local
##And Global Variable
name='This is a Global vaiable'
##Enclosing function example
def sayhello():
    #Declared name variable again here
    name = 'John'
    ##Enclosed another function here
    def hello():
        print('Hello '+name)
##Call function hello within function say hello
##The outer function must call the inner function
    hello()
##Call function say hello
sayhello()

##Now check for global variable by calling it outside any function
print(name)

##Built-in Python variables - cannot overwrite these
len









##Local/Global Variables Example
z = 50

def funcloc(z):
    #global z
    print('Value of z within the function is', z)
    z = -5
    print('Changed value of local z to', z)

funcloc(z)


print('z is still', z)

##Keyword Global

c=20
def globfun():
    global c
    print('Value of c is ', c)

globfun()

