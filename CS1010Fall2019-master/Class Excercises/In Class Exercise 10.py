# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:35:55 2019

@author: mushtu
"""

##In Class exercise
inventory = {'apples': 4.00, 'bananas' : 2.50, 'oranges': 5.80, 
             'pear' : 3.55, 'peach': 6.60}
inventory
del inventory['peach']
inventory
inventory['grapes'] = inventory['apples']*2
inventory
inventory['oranges'] -=1
inventory
inventory = {'apples': (4.00*1.15), 'bananas' : (2.50*1.15), 'oranges': (4.80*1.15), 
             'pear' : (3.55*1.15)}
inventory
len(inventory)