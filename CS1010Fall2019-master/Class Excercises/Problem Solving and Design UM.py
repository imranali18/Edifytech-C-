# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:01:19 2019

@author: mushtu
"""
##Find the minimum first and then its index
ls= [809,834,477,478,307,122,96,102,324,476]
#min(ls) 
low = min(ls)
min_index = ls.index(low)
print (min_index) 

















##Find Remove Find
def find_two_smallest(L): 
    'Return a tuple of the indices of the two smallest values in list L.'
    smallest = min(L) 
    min1 = L.index(smallest) 
    L.remove(smallest) 
    next_smallest = min(L) 
    min2 = L.index(next_smallest)
##Insert at index min1     
    L.insert(min1, smallest) 
    if min1 <= min2: 
        min2 += 1
    return (min1, min2)

L=[809,834,477,478,307,122,96,102,324,476]
find_two_smallest(L)




























##Sort, Identify Mins, Get Indices
def find_two_smallest(L):
    temp_list = L[:] 
    temp_list.sort() 
    smallest = temp_list[0] 
    next_smallest = temp_list[1] 
    min1 = L.index(smallest) 
    min2 = L.index(next_smallest) 
    return (min1, min2)
find_two_smallest(L)



















#Walk through the List
def find_two_smallest(L): 
# set min1 and min2 to the indices of the smallest and next-smallest 
# values at the beginning of L 
    if L[0] < L[1]: 
        min1, min2 = 0, 1 
    else: 
        min2, min1 = 1, 0
# examine each value in the list in order 
    for i in range(2, len(L)):
        if L[i] < L[min1]: 
            min2 = min1 
            min1 = i
# New second smallest? 
        elif L[i] < L[min2]: 
            min2 = i
    return (min1, min2)
find_two_smallest(L)

