# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:44:34 2019

@author: mushtu
"""

##Verify
A = {'a', 'b', 'd', 'e'}
B = {'b', 'c', 'e', 'f'}
C = {'d', 'e', 'f', 'g'} 
#Verify A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) 
#LHS
A | (B & C)
#RHS
(A | B) & (A | C)
 ##Verified that LHS = RHS