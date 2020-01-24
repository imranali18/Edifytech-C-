# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:17:04 2019

@author: mushtu
"""

##Part a
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

def scrabble_score(word):
     word=word.lower()
     total=0
     for let in word:
         total=score[let]+ total
     return total

scrabble_score("Hello")
scrabble_score("Today")
scrabble_score("Elephant")





##Part b
dict1 ={ 
    "L1":[87, 34, 56, 12], 
    "L2":[23, 00, 30, 10], 
    "L3":[1, 6, 2, 9], 
    "L4":[40, 34, 21, 67] 
}
dict2 ={ 
    "L1":["Welcome", "to", "RPI"], 
    "L2":["A", "computer", "science"], 
    "L3":["course", "for", "everyone"], 
} 
   

def sort_dict(dict):
    result=[]
    for i, j in dict.items(): 
        sorted_dict ={i:sorted(j)} 
        result.append(sorted_dict)
    return result

sort_dict(dict1)
sort_dict(dict2)
