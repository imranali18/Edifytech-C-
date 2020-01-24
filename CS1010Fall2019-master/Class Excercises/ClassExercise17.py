# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:17:12 2019

@author: mushtu
"""
##Problem 1
s=input("Enter string:")
count = 0
vowels = set("aeiouAEIOU")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)

















##Problem 2
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
    
    
    
    
#Problem 3
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)-set(s2))
print("The letters are:")
for i in a:
    print(i)
    
    
    
    
    

















#Problem 4
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)|set(s2))
print("The letters are:",a)
#for i in a:
#   print(i)























#Problem 5: Symmetric Difference
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Problem 6
list1=[1,2,3,4,5,6,6,6,4,3,2,2,4,4,8,9,10,20,21,22,20]
new=set(list1)
new
print(sum(new)/len(new))





















##Problem 7
E= {1,2,3,9,10,11,12}
F= {4,5,6,8,9,10,11,12,13}
##Cardinality
len(E|F)

















##Problem 8
m={1,3,5,7,9,11}
n={1,2,3,4,5,6,7}
print(m.symmetric_difference(n))
















#Problem 9
male_names = { 'Oliver', 'Declan', 'Henry' }
male_names.remove('Oliver')
male_names.add('Atlas')
male_names




















##Problem 10
male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }
#part a
all_names = male_names|female_names
all_names
len(all_names)
#part b
neutral_names= male_names & female_names
neutral_names
##part c
specific_names= male_names ^ female_names
specific_names
len(specific_names)





















































#In Class Exercise
C= list({2,3,5,7,8,10,17})
A=set([3,5,7,6])
B=set([2,8,17,10])
happy=len([x for x in C if x in A])
sad=len([i for i in C if i in B])
print (happy-sad)
