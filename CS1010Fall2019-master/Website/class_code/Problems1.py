# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:04:46 2019

@author: mushtu
"""
#Problem 1
name=input("What is your name? ")
print("Hello", name)

#Problem 2
name=input("What is your name? ")
age=int(input("How old are you? "))
year=2019+100-age
print(name, 'You will be 100 years old in the year',year)

##Problem 3
x=2
y=5
z=6
print('Average of the 3 numbers are', round((x+y+z)/3,2))

##Problem 4
x=int(input('Enter the first number '))
y=int(input('Enter the second number '))
#Part a
x!=y
#Part b
x==y

#Problem 5
name=input("What is your name?")
if (name=='Alice'or name=='Bob'):
    print("Hello", name)
else:
    print('Hello')
    
#Problem 6
n=int(input("Enter the number "))
b=input("Enter A for addition,M for Multiplication")
if (b=='A'):
    print('Result of addition is',n+(n-1))
elif (b=='M'):
    print('Result of multiplication is',n*(n-1))
else:
    print('Invalid input')
    
#Problem 7
n=int(input("Enter the number "))
if (n%2==0):
    print('This number is even')
else:
    print('This number is not even')

#Problem 8
n=int(input('Number of friends?'))
m=int(input('Number of chocolates in the packet?'))
if (m<n):
    print('Number of chocolates insufficient')
elif (m%n)==0:
    print('Each friend gets', int(m/n),'chocolates')
else:
    print('There is a surplus of ',m%n, 'chocolates')
    












