# import sys
# sys.path.append('/home/lt/FJ_ML2018summer/venv/lib/python3.6/site-packages')
# import sys
# print(sys.path)
from PIL import Image
img = Image.open(path)
img.show()
print(img.size[0],img.size[1])
for x in range(img.size[0]):
    for y in range(img.size[1]):
        r,g,b = img.getpixel((x,y))
        img.putpixel((x,y),( int(r/2),int(g/2),int(b/2) ))
img.save("Q2.jpg")
img.show()