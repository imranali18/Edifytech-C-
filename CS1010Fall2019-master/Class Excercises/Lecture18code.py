# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:44:53 2019

@author: uzmam
"""
import time
start_time=time.time()

ls=[809,834, 477, 478, 307, 122, 96, 102, 324, 476]
low=min(ls)
min_index=ls.index(low)
print(min_index)

end_time=time.time()
elapsed_time=end_time-start_time
print(elapsed_time)
#Find remove find

'''This function returns a tuple of the two lowest values 
   in list L'''
def find_two_smallest(L):
    smallest=min(L)
    min1=L.index(smallest)
    L.remove(smallest)
    next_smallest=min(L)
    min2=L.index(next_smallest)
    #Insert at index min1
    L.insert(min1,smallest)
    if min1<=min2:
        min2+=1
    return (min1,min2)

L=[809,834, 477, 478, 307, 122, 96, 102, 324, 476]
print(find_two_smallest(L))

'''Sort, Identify mins, get indices'''
def find_two_smallest(L):
    temp_list=L[:]
    temp_list.sort()
    smallest=temp_list[0]
    next_smallest=temp_list[1]
    min1=L.index(smallest)
    min2=L.index(next_smallest)
    return (min1,min2)
L=[809,834, 477, 478, 307, 122, 96, 102, 324, 476]
print(find_two_smallest(L))
   
'''Walking through the list'''  
def find_two_smallest(L):
    if L[0]<L[1]:
        min1,min2=0,1
    else:
        min2,min1=0,1
    for i in range(2,len(L)):
        if L[i]<L[min1]:
            min2=min1
            min1=i
        elif L[i] < L[min2]:
            min2=i
    return (min1,min2)
    
L=[809,834, 477, 478, 307, 122, 96, 102, 324, 476]
print(find_two_smallest(L))
       
'''Find the mode of a given set of numbers
   Mode: Number that occurs the most number of times'''   
L=[(2,3),(5,1),(2,2),(4,5),(3,4),(2,5),(1,2),(3,1)]
'''Modify input'''
L1=[]
for i in L:
    L1.append(i[0])
    L1.append(i[1])
print(L1)
'''Actual Solution'''    
Final=[]
temp=[] 
for i in range(len(L1)):
    if L1[i] not in temp:
        number=L1[0]
        count=0
        for j in range(len(L1)):
            if L1[i]==L1[j]:
                count+=1
        Final.append([L1[i],count])
        temp.append(L1[i]) #optional step
print(Final)   

temp2=[]
for val in Final:
    temp2.append(val[1])
new=max(temp2)

mode=[]
for val2 in Final:
    if new==val2[1]:
        mode.append(val2[0])
print(mode)

print(L1)
L1.sort()

 
'''Sorting and then finding the mode'''   
curr=0 #Count value, current max
index=0
prev=-1
count=0
modes=[]
while index < len(L1) :
    if L1[index]!=prev:
        if count>curr:
            modes=[prev]
            curr=count
        elif count==curr:
            modes.append(prev)
        prev=L1[index]
        count=1
    else:
        count+=1
    index+=1

print(modes)
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    