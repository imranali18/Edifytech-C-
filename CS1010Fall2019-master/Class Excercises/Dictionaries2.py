# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:35:44 2019

@author: mushtu
"""

# Dictionary nested inside a dictionary nested inside a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}

# Accessing values by calling the keys
d['key1']['nestkey']['subnestkey']











# Empty nested dictionary 
Dict = { 'Dict1': { },  
         'Dict2': { }} 
print(Dict) 
 












 
# Nested dictionary having same keys 
Dict = { 'Dict1': {'name': 'Ali', 'age': '19'}, 
         'Dict2': {'name': 'Bob', 'age': '25'}} 
print(Dict) 














  
# Nested dictionary of mixed dictionary keys 
Dict = { 'Dict1': {1: 'G', 2: 'F', 3: 'G'},  
         'Dict2': {'Name': 'Geeks', 1: [1, 2]} } 
print(Dict) 
















# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}
# Method to return a list of all keys 
d.keys()
# Method to grab all values
d.values()
# Method to return tuples of all items
d.items()











# Python code to demonstrate working of 
# str() and items() 
  
# Initializing dictionary 
dict1 = { 'Name' : 'Sam', 'Age' : 21 } 
  
# using str() to display dict1 as string 
print ("The constituents of dictionary as string are : ") 
print (str(dict1)) 
  
# using str() to display dict1 as list 
print ("The constituents of dictionary as list are : ") 
print (dict1.items()) 












# Python code to demonstrate working of 
# len() and type() 
  
# Initializing dictionary 
dict1 = { 'Name' : 'Sam', 'Age' : 21, 'ID' : 2541997 } 
  
# using len() to display dic size 
print ("The size of dic is : ",end="") 
print (len(dict1)) 
  
# using type() to display data type 
print ("The data type of dic is : ",end="") 
print (type(dict1)) 









# Python code to demonstrate working of 
# clear() and copy() 
  
# Initializing dictionary 
dict1 = { 'Name' : 'Dan', 'Age' : 19 } 
  
# Initializing dictionary  
dict3 = {} 
  
# using copy() to make shallow copy of dictionary 
dict3 = dict1.copy() 
  
# printing new dictionary 
print ("The new copied dictionary is : ") 
print (dict3.items()) 
  
# clearing the dictionary 
dict1.clear() 
dict1  
# printing cleared dictionary 
print ("The contents of deleted dictionary is : ",end="") 
print (dict1.items()) 




















# Python code to demonstrate working of update()   
# Initializing dictionary 1 
dict1 = { 'Name' : 'Jon', 'Age' : 20 } 
  
# Initializing dictionary 2 
dict2 = { 'ID' : 2541997 } 
  
# using update to add dict2 values in dict 1 
dict1.update(dict2) 
dict1  

w={"house":"Haus","cat":"Katze","red":"rot"}
w1 = {"red":"rouge","blau":"bleu"}
w.update(w1)
w









# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'RPI', 
        'A' : {1 : 'RPI', 2 : 'For', 3 : 'CS'}, 
        'B' : {1 : 'Great', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
 







 
# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
  
# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 
 






 
# Deleting a Key  
# using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 
  
# Deleting a Key-value pair 
# using popitem() 
Dict.popitem() 
print("\nPops first element: ") 
print(Dict) 
 







 
# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 














##For loops
d = {'Red': 1, 'Green': 2, 'Blue': 3}
for k in d:
    print(k,' corresponds to ',d[k])








##another way
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 




##Only keys
for k in d.keys():
	print (k)

#Only values    
for j in d.values():
	print (j)
    













    
##Lists to Dictionary

dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
##List comprehension
name_to_value_dict = {key:value for key, value in zip(countries, dishes)}
name_to_value_dict

##Another method:for loop
name_to_value_dict = {}
for key, value in zip(countries, dishes):
        name_to_value_dict[key] = value
name_to_value_dict














##Problem 1
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)


























##Problem 2
dictionary={'one':5, 'two':1, 'three':6, 'four':10}
val = list(dictionary.values()) 
val.sort() 
res = val[-2] 
print(res) 


























##Problem 3
# stores name and corresponding salaries 
salary = {"emp1" : 50000, "emp2" : 60000, "emp3" : 5000}  
  
# stores the salaries only 
list1 = salary.values()  
print(sum(list1))  # prints the sum of all salaries 


























##Problem 4

# Python3 code to demonstrate  
# getting selective dictionary keys 
# using list comprehension 
  
# initializing dictionary 
test_dict = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}  
# initializing selective list keys  
select_list = ['C', 'D']   
# using list comprehension 
# getting selective dictionary keys  
res = [test_dict[i] for i in select_list if i in test_dict] 
  
# printing result  
print ("The selected values from list keys is : " +  str(res)) 


##Method 2

# Python3 code to demonstrate  
# getting selective dictionary keys 
# using set.intersection() 
  
# initializing dictionary 
test_dict = {"A" : 1, "B" : 2, "C" : 3, "D" : 4}   
# initializing selective list keys  
select_list = ['C', 'D']   
# using set.intersection() 
# getting selective dictionary keys  
temp = list(set(select_list).intersection(test_dict)) 
res = [test_dict[i] for i in temp] 
res 
# printing result  
print ("The selected values from list keys is : " + str(res)) 



































#Problem 5
##Method 1
# Python3 code to demonstrate 
# Element Occurrence in dictionary value list 
# using list comprehension + sum()  
# initializing dictionary 
test_dict = { "A" : [1, 4, 5, 3], 
              "B" : [4, 6], 
              "C" : [5, 2, 1] } 
  
# initializing test list  
test_list = [2, 1] 
  
# using list comprehension + sum() 
# Element Occurrence in dictionary value list 
res = {idx : sum(1 for i in j if i in test_list) 
                for idx, j in test_dict.items()} 
res  
# print result 
print("The summation of element occurrence : " + str(res)) 

##Method 2

# Python3 code to demonstrate 
# Element Occurrence in dictionary value list 
# using collections.Counter() 
from collections import Counter 
  
# initializing dictionary 
test_dict = { "A" : [1, 4, 5, 3], 
              "B" : [4, 6], 
              "C" : [5, 2, 1] } 
  
# initializing test list  
test_list = [2, 1] 
# using collections.Counter() 
# Element Occurrence in dictionary value list 
# omits the 0 occurrence word key 
res = (Counter(j for j in test_dict 
           for i in test_list if i in test_dict[j])) 
res  
# print result 
print("The summation of element occurrence : " + str(res)) 
