# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:44:28 2019

@author: mushtu
"""
#Problem 1a
def f1(subs1,str1):
    if subs1 in str1:
        return True
    return False

subs1='ello'
str1='Hello World!'
f1(subs1,str1)












##Problem 1b
l1=['a','b','c','d','r']
s1='c1tdoorrbin'
count=0
for i in range(len(l1)):
    if l1[i] in s1:
        count+=1
print(count)
        













##Problem 2
n=25   
for i in range(n):
    if i%2==0:
        print(i, end=" ")






#Alternate way:
for i in range(0,n,2):
        print(i)
        
     
        
        
        
        
        
        
        
        
        
        
        
#Problem 3
word = input("Input a word to reverse: ") 
for char in range(len(word)-1, -1, -1): 
         print(word[char], end="") 















#Problem 4
def string_subs(sub,string1):
    results = 0
    sub_len = len(sub)
    for i in range(len(string1)):
        if string1[i:i+sub_len] == sub:
            results += 1
    print (results)



string1 = 'catdogelephantdogeleph'
sub = 'eleph'
string_subs(sub,string1)




















#Problem 5
def has22(a):
    for i in range(len(a)):
        if a[i]==2 and (len(a)-i)>1:
            if a[i]==a[i+1]:
                return True
    return False      
  
has22([1, 2, 2])          
has22([1, 2, 1, 2])            
has22([2, 1, 2])            
  




















         




##Problem 6
def end_other(a, b):
  a=a.lower()
  b=b.lower()
  if len(a)>=len(b):
    if a.endswith(b):
      return True
    return False
  else:
    if b.endswith(a):
      return True
    return False


end_other('Hiabc', 'abc') 
end_other('AbC', 'HiaBc') 
end_other('abc', 'Hiabcx') 


























#Problem 7
for fizzbuzz in range(50):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
    
    
    
    
    
    
 
    
    
    
    
    
    
    
#Problem 8
s = input("Input a string  ")
d=0
l=0
for c in s:
#built in method for checking strings
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)    
    
    
    
    
    
    
    
    
    
    
    




























    
#In_Class exercise    
def cat_dog(string1):
    count_cat=0
    count_dog=0
    for i in range(len(string1)):
        if string1[i:i+3] == 'cat':
            count_cat += 1
        if string1[i:i+3] == 'dog':
            count_dog += 1
    if count_cat==count_dog:
        return True
    return False

cat_dog('catdog')
cat_dog('catcat')
cat_dog('1cat1cadodog')
