# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:14:36 2019

@author: mushtu
"""

student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
'id5': 
   {'name': ['Dan'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
'id6': 
   {'name': ['Dan'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   }
}


result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
len(result)
