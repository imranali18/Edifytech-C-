# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:33:19 2019

@author: mushtu
"""

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)


