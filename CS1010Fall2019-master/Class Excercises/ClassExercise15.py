# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:08:24 2019

@author: mushtu
"""
#We simply open a file called “Classex1.txt”. It must exist in 
#the current directory (ie, the directory you are running the
#code from).
#The r means the file will be opened in a read only mode. 
#Other common modes are w for write, a for append. 

f=open('Classex1.txt','r')
data = f.read()
f.close()











##After reading the file contents into a variable data 
#We closed it	
print(data)










##Using the built in funtion split to split on spaces
words = data.split(" ")
print("The words in the text are:")
print(words)
num_words = len(words)
print("The number of words is ", num_words)











## Using similar logic we count lines but split by \n
lines = data.split("\n")
print("The lines in the text are:")
print(lines)
print("The number of lines is", len(lines))











 ##If there is space in between lines then that is also counted
#as a new line so we need to get rid of that
for l in lines:
    if len(l)==0:
       lines.remove(l) 
##Now check again       
print("The number of lines is", len(lines))









##Problem 2
##Method 1
wood = 'How much wood would a woodchuck chuck if a woodchuck couldchuck wood?'
wood=wood.split()
woolist = []
for x in wood:
    if 'woo' in x:
        woolist.append(x)
print(woolist)


##Method 2:List comprehensions
[x for x in wood if 'woo' in x]










##Problem 3
[x for x in wood if len(x) >= 5]













##Problem 4
[x.upper() for x in wood if 'wo' in x] 












##Problem 5
[x+'-away' for x in wood if len(x) <= 4]













##Problem 6
[(x, len(x)) for x in wood if len(x) >=5] 











