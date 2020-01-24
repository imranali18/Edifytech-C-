# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:36:10 2019

@author: mushtu
"""
##Problem 1
x=23
while x in range(23,50):
    print(x)
    x+=1
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
##Problem 2    
x=23
while x in range(23,50):
    if x%2==0:
        print(x, end=' ')
    x+=1
















##Problem 3
x=1952
while x<2020:
    x+=4
    print(x, end=' ')













    
#Problem 4
x=10
while x>=1:
    print(x, end=' ')
    x-=1
    














    
##Problem 5    
a = 0
while a < 101:
    print('*', end=' ')
    a+= 1
print()











##Problem 6
l1=[1,2,3,4]
l2=[-2,3,1,0]
l3=[]
i=0
while i<len(l1):
    y=l1[i]+l2[i]
    l3.append(y)
    i+=1
print(l3)










#Problem 7 Print rectangle
a = 0 ##line number
while a < 5:
    b=0  ## number of stars
    while b<5:
        print('*', end='')
        b+=1
    print()
    a+= 1

 
    
    
    
    
    
    
    
    
##Problem 8
Rat1=[1,3,2,2,1,3,4,2,1,1]
Rat2=[2,1,1,3,2,2,2,1,1,2]
days=[]
i=0
while i<10:
    if Rat1[i]>Rat2[i]:
        days.append(i+1)
    i+=1
print(days)
    












##Problem 9: Guessing game
import random
target_num = random.randint(1, 10)
guess_num=0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')

















#Problem 10
items = []
i=100
while i in range(100, 401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        items.append(s)
    i+=1
print( ",".join(items))

#The join() method takes all items in an iterable and joins them into one string.
#A string must be specified as the separator.














##class exercise
num=int(input("enter a number "))
factors=[]
i=1
while i <=num+1:
    if num%i==0:
       factors.append(i)
    i+=1
print (factors)
    
