# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:31:00 2019

@author: mushtu
"""

##Submitted exercise
f=open('Classex.txt','r')
data = f.read()
f.close()
##After reading the file contents into a variable data 
#We closed it	
print(data)
words = data.split(" ")
print(words)

##Counter of vowels 
count=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in words:
    for j in i:
        if j in vowels:
            count=count+1
print(count)
        
    