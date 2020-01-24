# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:39:21 2019

@author: mushtu
"""
##Problem 1
def first_last6(nums):
  if len(nums)<1:
    return 
  else:
    if (6 in nums):
      if nums[0]==6 or nums[-1]==6:
        return True
      return False
    return False

##Test cases
first_last6([1, 2, 6])
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3])






##Problem 2
def common_end(a, b):
  if len(a)>0 and len(b)>0:
    if a[0]==b[0] or a[-1]==b[-1]:
      return True
    return False
  return False

##Test cases
common_end([1, 2, 3], [7, 3])
common_end([1, 2, 3], [7, 3, 2])
common_end([1, 2, 3], [1, 3])







##Problem 3
def big_diff(nums):
  a=max(nums)
  b=min(nums)
  return a-b

##Test cases
big_diff([10, 3, 5, 6]) 
big_diff([7, 2, 10, 9])
big_diff([2, 10, 7, 2])










##Problem 4
def rotate_left3(nums):
  num=[1,2,3]
  num[0]=nums[1]
  num[1]=nums[-1]
  num[2]=nums[0]
  return num


##Test
rotate_left3([1, 2, 3]) 
rotate_left3([5, 11, 9]) 
rotate_left3([7, 0, 0])



##Problem 5
a=[1,3,5]
a.insert(1,2)
a
a.insert(3,4)
a

b=[3,4,6,9]
b.remove(9)
b


c=[5,9,3,2,1]
c.reverse()
c


d=[7,9,12,3,2,0,8]
d.sort()
d


e=[1,2,3,4]
e.append(5)
e


f=[9,10,11]
f.pop()
f
