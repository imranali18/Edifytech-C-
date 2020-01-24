# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:53:47 2019

@author: mushtu
"""

from PIL import Image
filename="Flower.jfif"
im = Image.open(filename)
im.show()

##Grayscale
gray_im = im.convert('L')
gray_im.show()

##Copy paste
gray_im.size
##Rescale to half
#Resize the image
scaled = gray_im.resize((280,210))
scaled.show()
##New Image
im5 = Image.new('RGB', (280*2, 210*2))
im5.show()
im5.paste( scaled, (0,0))   ##not assigning the result of paste to a new variable
im5.show()
im5.paste( scaled, (280,0 ))
im5.show()
im5.paste( scaled, (0,210 ))
im5.show()
im5.paste( scaled, (280,210 ))
im5.show()
##Save this
im5.save(filename + "_Homework.jpg")
