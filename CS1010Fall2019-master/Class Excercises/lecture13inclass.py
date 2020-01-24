# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:08:37 2019

@author: mushtu
"""

A="Meka's Lounge|5|2|4"
B="Tosca Grille|1|2|2"
C="Happy Lunch |3|4|5"
A=A.split('|')
A_average=round((int(A[1])+int(A[2])+int(A[3]))/3,2)
print(A)
B=B.split('|')
print(B)
B_average=round((int(B[1])+int(B[2])+int(B[3]))/3,2)
C=C.split('|')
print(C)
C_average=round((int(C[1])+int(C[2])+int(C[3]))/3,2)
##Driver program
L=[[A[0],A_average],[B[0],B_average],[C[0],C_average]]
print(L)
##Append to the list
D="Dinosaur Bar-B-Que|5|4|5"
D=D.split('|')
print(D)
D_average=round((int(D[1])+int(D[2])+int(D[3]))/3,2)
L.append([D[0],D_average])
print(L)
