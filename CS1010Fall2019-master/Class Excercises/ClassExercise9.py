# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:50:41 2019

@author: mushtu
"""
##Problem 1
def same_first_last(nums):  
     if len(nums)>0:    
         if nums[0]==nums[-1]:      
             return True    
         return False  
     return False


#Test
same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])










##Problem 3

def max_end3(nums):
  newlist=[nums[0],nums[-1]]
  newelement=max(newlist)
  l=[newelement]*len(nums)
  return l













##Problem 5
def row_col(x,y):
    a=x[0][0]+y[0][0]
    b=x[0][1]+y[1][0]
    c=x[0][2]+y[2][0]
    return [a,b,c]

x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[9,8,7],[6,5,4],[3,2,1]]
row_col(x,y)














##Problem 6
def sublist(l1,l2):
    if l2[0] in l1:
        return True
    return False

sublist([1,2,3,4,5],[2,3])
sublist([3,5,7],[6,7])




















#Problem 7
def max_of_list(a,b):
    new=max(a)
    if new<=b:
        return True
    return False

max_of_list([20,12,31, 15],22)
max_of_list([35,42,68,10],75)
max_of_list([57,29,6,100],100)






















##Problem 8
def find_index(a,b):
    if b in a:
        return a.index(b)
    return False

find_index([1,2,4],4)
find_index([5,6,7,8],9)
find_index([15,63,81,93,99],99)
find_index([1,2,4,5],6)









































##In Class exercise
def middle_way(a,b):
    if len(a)%2==0:
        element_of_a=(len(a)//2)
        elementa=(a[element_of_a]+a[element_of_a-1])/2
    else:
        elementa=a[(len(a)//2)]
    if len(b)%2==0:
        element_of_b=(len(b)//2)
        elementb=(b[element_of_b]+b[element_of_b-1])/2
    else:
        elementb=b[(len(b)//2)]
    return [elementa,elementb]

middle_way([1, 5, 3, 4], [4, 5, 6]) 
middle_way([7, 7, 7], [3, 8, 0, 5])
middle_way([5, 2, 9], [1, 4, 5])
middle_way([1,4,2,5,8],[2,4])
middle_way([1,5,3,7,8,9,10],[2,3,1])



