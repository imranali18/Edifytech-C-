# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:26:01 2019

@author: mushtu
"""

##Create empty dictionary
empty = {}
type(empty)
















##Create dictionary food
food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
food

















##Other ways of creating dictionaries
new= dict(Bob='508-2232', John='159-0055')
new
new1=dict([('Bob', '508-2232'), ('John', '159-0055')])
new1




























## Lookuptag: Creating dictionaries by assignment
bag = dict()
bag['money'] = 12
bag['candy'] = 3
bag['tissues'] = 75
bag















##Constructing and accessing dictionaries
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}




# Call values by their key
my_dict['key2']
print (bag['candy'])


















#Different object types for key value pair
my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
# Let's call items from the dictionary
my_dict['key3']
# Can call an index on that value
my_dict['key3'][1]

















##Using mutable objects
dict1 = { [1,2,3]:"abc"}
##Can use tuples for keys
dict1 = { (1,2,3):"abc", 3.1415:"abc"}
dict1














##Operators
my_dict = {'Ahmad': 10, 'Jane': 42, 'Carol': 39, 'Jon': 25}
len(my_dict)
del my_dict['Ahmad']
my_dict

















##Affecting values
my_dict['key1']= 123
my_dict
# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123
#Check
my_dict['key1']
my_dict
##Using -= or +=
# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
my_dict['key1']
my_dict














##Problem 1
newdict= {0: 10, 1: 20}
newdict[2] = 30
newdict











##Problem 2
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
      
is_key_present(5)
is_key_present(9)



















##Problem 3
myDict = {'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict: 
    del myDict['a']
print(myDict)













