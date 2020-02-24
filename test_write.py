image_filename = "1.jpg"
text_filename = "abc.txt"
output_image_filename = "out.png"
from lib import *

def double_range(limit1, limit2): #y - x
    """Produce all pairs in (0..`limit1`-1, 0..`limit2`-1)"""
    for i1 in range(limit1):
        for i2 in range(limit2):
            yield i1, i2

from PIL import Image
print("--PROCCES STARTED")

# load files
img = Image.open(image_filename)
print("#image loaded")
file = open(text_filename, 'r')
print("#txt loaded")

#read txt file
input = file.read()
bin_data = []
for i in input:
    bin_data.append(search(i, "str>bin"))
print("#txt read done")

print("-------------first word is " + bin_data[0])

# check img
img = img.convert("RGBA")
if img.width*img.height < len(bin_data)*7 :
    print ("IMAGE TOO SMALL, CHOOSE BIGGER IMAGE")
    exit()
print("#img size check done")


# main algorithm
x=0
y=0

alpha_channel = Image.new('L', img.size, 255)

for temp_word in bin_data :
    for i in temp_word:
        alpha_channel.putpixel((x,y), (255 - int(i)))
        # print(alpha_channel.getpixel((x,y)))
        # print(x, "-", y )
        x+=1
        if x == img.width :
            y+=1
            x=0

img.putalpha(alpha_channel)

print("#algorithm done")

img.save(output_image_filename)
print("#img saved")
print("--PROCCES FINISHED")
