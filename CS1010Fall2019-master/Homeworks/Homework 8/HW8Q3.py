# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:52:22 2019

@author: mushtu
"""

def ask():
    
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
        
    print('Thank you, your number squared is: ',n**2)