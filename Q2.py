# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:15:27 2018

@author: admin
"""

from PIL import Image
img = Image.open("/home/User/Documents/westbrook.jpg")
img.show()
print(img.size[0],img.size[1])
for x in range(img.size[0]):
    for y in range(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),( int(r/2),int(g/2),int(b/2) ))
img.save("/home/User/Documents/Q2.jpg")
img.show()
