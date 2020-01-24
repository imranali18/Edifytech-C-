#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:07:30 2019

@author: uzma
"""

# Entire phrase 
'This is a new string'

# We can also use double quote
"This string is built with double quotes"

# Be careful with quotes!
' I'm using single quotes, but this will create an error'

"Now I'm ready to use the single quotes inside a string!"

##Print statements
print('Hello World 1')
print('Hello World 2')
print('Use \n to print a new line')
print('\n')

# Assign s as a string
s = 'Hello World'
# Print the object
print(s) 





#Length
len(s)
##Indexing
# Show first element (in this case a letter)
s[0]
##Show the last element
s[len(s)-1]
s[len(s)-1]
s[10]
s[-1]
s[-2]
##Slicing
# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]
# Note that there is no change to the original s
s
# Grab everything UP TO the 4th index (will not include 4th index)
s[:4]
#Everything
s[:]
# Last letter
s[-1]
# Grab everything but the last 2 letters
s[:-2]
##Grab the last 3 letters/characters
s[-3:]
# Grab everything, but go in steps size of 1
s[::1]
# Grab everything, but go in step sizes of 2
s[::2]
# Concatenate strings!
s + ' concatenate me!'
# We can reassign s completely though!
s = s + ' concatenate me!'
s+='concatenate me!!'
print(s)
##Repitition
letter = 'u'
letter*10











##Built in Methods
##Already in Python
# Upper Case a string
s.upper()
# Lower case
s.lower()
# Split a string by blank space (this is the default)
s.split()
# Split by a specific element (doesn't include the element that was split on)
s.split('H')
##Replace
s.replace(s[1], 'e')
##End and start
s.endswith('World')
s.startswith('World')
##Test for substrings
'a' in 'program'
'e' in 'program'
'a' not in 'program'








##Formatting
##Method 1
print("I'm going to inject %s here." %'something')

print("I'm going to inject %s text here, and %s text here." %('some','more'))

##Pass variable name
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

#Two methods
print('He said his name was %s.' %'Fred')
print('He said his name was %r.' %'Fred')

#Tab
print('I once caught a fish %s.' %'this \tbig')
print('I once caught a fish %r.' %'this \tbig')

##More formatting
print('I wrote %s programs today.' %3.75)
print('I wrote %d programs today.' %3.75)  

print('Floating point numbers: %5.2f' %(15.144))
print('Floating point numbers: %1.0f' %(15.144))
print('Floating point numbers: %.3f' %(15.144))






##The .format method
print('This is a string with an {}'.format('insert'))

print('The {2} {1} {0}'.format('fox','brown','quick'))

print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))

print('A {p} saved is a {p} earned.'.format(p='penny'))










##The f-string method
name = 'Uzma'
print(f"She said her name is {name}.")


print(f"She said her name is {name!r}")
