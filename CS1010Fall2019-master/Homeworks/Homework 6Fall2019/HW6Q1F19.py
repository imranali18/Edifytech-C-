# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:42:54 2019

@author: mushtu
"""

def smallest_two(mylist):
     mylist.sort()
     newlist = []
     if len(mylist) > 0:
         newlist.append(mylist[0])
         if len(mylist) > 1:
             newlist.append(mylist[1])
     return newlist

values = [35, 34, 20, 40, 60, 30]
print(smallest_two(values))