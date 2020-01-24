# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:49:06 2019

@author: mushtu
"""
#Strip
x = "blue! Sky is blue! Sky is blue! Sky is blue!"
#strip method
x.strip('lbue!')
print(x)
x.lstrip('blue!')
x.rstrip('blue')
x='\n    Hello World    \t'
x.strip(" ")
#Split
y='Hello|World|Hello|Python'
y.split("l")
#Find method
x = "blue! Sky is blue! Sky is blue! Sky is blue!"
x.find('Sky',7,15)
##converting strings to list
s='Hello'
s=list(s)
str(s)
#.join method
''.join(s)
l=['Hello','Python','RPI']
' '.join(l)