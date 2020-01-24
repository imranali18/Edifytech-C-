#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:51:50 2019

@author: uzma
"""
##Practice Question 1
print('What is your name?')
name=str(input())
print('Hello', name)


##Question 2
print('What is your name?')
name=str(input())
if name==('Alice' or 'Bob’):
    print('Hello', name)
else:
    print(‘Hello’)
    
    
    
##Question 3
print('Please enter the number')
a=int(input())
print('For addition enter A; for multiplication enter M')
b=str(input())
if b=='A':
    a=a+(a-1)
    print ('Result of addition is ', a)
else:
    a=a*(a-1)
    print ('Result of multiplication is ', a)

##Question 4
print('Enter the number')
a=int(input())
if a%2==0:
    print('This is an even number')
else:
    print('This is not an even number')

##Question 5
print('How many friends are invited?')
a=int(input())
print('How many chocolates are there in this packet?')
b=int(input())
if b<a:
    print('You are short of ',a-b, 'chocolates')
elif b%a==0:
     c=b/a
     print('Chocolates will be evenly distributed and each friend gets',c, 'chocolates' )
else:
    d=b%a
    print('Chocolates cannot be evenly distributed because you have a surplus of ', d, 'chocolates')


