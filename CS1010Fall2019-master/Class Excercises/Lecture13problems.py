# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:46:58 2019

@author: mushtu
"""

#problem 1
def same_first_last(x):
    if len(x)>1:
        if x[0]==x[-1]:
            return True
    return False

print(same_first_last([1,2,3,1]))

#problem 3
def max_end3(l):
    s=max(l[0],l[-1])
    return [s]*len(l)

print(max_end3([1,2,4,3]))

#problem 4
def middle_way(a,b):
    return [a[1],b[1]]

print(middle_way([1,2,3],[4,5,6]))

#Problem 5
X = [[1,2,3],[4 ,5,6], [7 ,8,9]] 
Y = [[9,8,7],[6,5,4],[3,2,1]] 
print([X[0][0]+Y[0][0],X[0][1]+Y[1][0],X[0][2]+Y[2][0]])

#Problem 6
sub_list=[1,10]
List=[1,2,3,4]
sub_list[0] in List

#Problem 7
List=[20,5,4,21]
Value=22
max(List)>=Value
List=[35,42,68,10]
Value = 68 



