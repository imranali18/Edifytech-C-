# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:29:24 2019

@author: mushtu
"""

def is_friend_present(x):
    phonebook={'sam': 999122222,'tom': 111222222,'harry':123333333}
    if x in phonebook:
      print(phonebook [x])
    else:
      print('Not Found')
      
is_friend_present('sam')
is_friend_present('Uzma')
