# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 20:28:41 2019

@author: mushtu
"""

x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for (key, value) in set(x.items()) & set(y.items()):
    print('%s: %s is present in both x and y' % (key, value))