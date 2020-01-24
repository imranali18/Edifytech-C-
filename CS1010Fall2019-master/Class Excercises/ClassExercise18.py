# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:19:18 2019

@author: mushtu
"""

##Problem 1
import collections
f=open('Dict.txt','r')
data = f.read()
f.close()
c = collections.Counter(data)
c














##Problem2
def prob2(x):
    import collections
    y=collections.Counter(x)
    for values in y.values():
        if values != 1:
            return False
    return True
            
prob2('abcdef')
prob2('abbcdef')






















##Problem 3
def prob3(x,y):
    import collections
    x1=collections.Counter(x)
    y1=collections.Counter(y)
    if x1==y1:
        return True
    return False

prob3('abcd','cdba')
prob3('abcde','cdba')
      



















##Problem 4
# Declare hash function/ dictionary       
 key_value ={}     
# Initializing value  
 key_value[2] = 56       
 key_value[1] = 2 
 key_value[5] = 12 
 key_value[4] = 24
 key_value[6] = 18      
 key_value[3] = 323 
key_value
for i in sorted (key_value.values()) :  
     print(i, end = " ") 
  
 
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Problem 5
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): 
    dic4.update(d)
print(dic4)
    























##Problem 6
my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict.keys():    
    result=result * my_dict[key]
print(result)













##Problem 7
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))
    
    
    
 
    
    
    
    
    
    
    
    
    
    
##About the join operator    
# elements with a character.   
list1 = ['1','2','3','4']   
s = "-"  
# joins elements of list1 by '-' 
# and stores in sting s 
s = s.join(list1)  
# join use to join a list of 
# strings to a separator s 
print(s)     
# Joining with empty separator 
list1 = ['s','c','h','o', 'o','l']  
print("".join(list1))     
    
    





    
    
##Problem 8    
def rot13_decode(secret):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    words = [words for words in secret.split()]
    results = []
    for word in words:
            results.append("".join([key[char] if char in key.keys() else char for char in word]))
    return " ".join(results)


rot13_decode('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')   


































  
##In class exercise
def palin(x):
    import collections
    y=collections.Counter(x)
    flag=0
    for i in y.values():
        if i%2!=0:
            flag+=1
    if flag > 1:
        return False
    return True
        
palin('tact coa')
palin('moon')        
palin('xxxyy')             
palin('mom') 
palin('runnurses') 
