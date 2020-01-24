# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:08:08 2019

@author: mushtu
"""
##Initialization
import collections

print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b','c','a']))
print (collections.Counter({'a':2, 'b':3, 'c':1}))
print (collections.Counter(a=2, b=3, c=1))














import collections

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabets')

print ('C1:', c1)
print ('C2:', c2)

print ('\nCombined counts:')
print (c1 + c2)

print ('\nSubtraction:')
print (c1 - c2)

print ('\nIntersection (taking positive minimums):')
print (c1 & c2)

print ('\nUnion (taking maximums):')
print (c1 | c2)









##Another technique
c = collections.Counter('abcdaab')
c
for letter in 'abcde':
    print ('%s : %d' % (letter, c[letter]))
    
    
    
    
    
    
    
    
    