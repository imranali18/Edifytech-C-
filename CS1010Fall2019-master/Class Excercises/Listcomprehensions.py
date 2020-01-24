# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:01:55 2019

@author: mushtu
"""

# Grab every letter in the string 'computer'
new = [x for x in 'computer']
new













# Cube numbers in range and turn into list
new1 = [x**3 for x in range(0,8)]
new1















# Check for all even numbers in a range
new2 = [x for x in range(8) if x % 2 == 0]
new2















##Check for odd numbers
new3 = [x for x in range(8) if x % 2 != 0]
new3




















# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]

fahrenheit










##Nested list comprehensions
##We have the following list
ls=[x**2 for x in range(11)]
ls
##Square of the list above
new4 = [ x**2 for x in [x**2 for x in range(11)]]
new4

















##Lambda function
sum1 = lambda x, y : x + y
sum1(3,4)














##Temperature conversion
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
 
def celsius(T):
    return (float(5)/9)*(T-32)
 
temperatures=(36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheit, temperatures))
C = list(map(celsius, F))
print(F)
print(C)









##By using lambda, we wouldn't have had to define and name the 
##functions fahrenheit() and celsius() because lambda needs 
#an expression only
C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
C = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C)










##More examples with map()
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
list(map(lambda x, y : x+y, a, b))

list(map(lambda x, y, z : x+y+z, a, b, c))

list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))











##Filter function
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2!=0, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)













## I/O with files
# Open the Test.txt we made earlier
my_file = open('Test.txt','r')
# We can now read the file
my_file.read()
##what happens if we try reading it again
# We can now read the file
my_file.read()
#This happens because you can imagine 
#the reading "cursor" is at the end of the file after having read it.
#So there is nothing left to read. We can reset the "cursor" like this:
# Seek to the start of file (index 0)
my_file.seek(0)
my_file.read()
# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readline()
my_file.readlines()
##It is a good practice to close the file after use
my_file.close()








##Writing a file
title = 'Story of my life \n'
##Write the contents of Test.txt into a new file
path = 'C:\\Users\\mushtu\Test.txt'
new_file = open(path,'r')
new = new_file.read()
##Newtest does not exist: we will create and write into it
new_path = 'C:\\Users\\mushtu\ Newtest.txt'
final_file = open(new_path,'w')
final_file.write(title)
print(title)
final_file.write(new)
print(new)

final_file.close()
new.close()
