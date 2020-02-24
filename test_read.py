image_filename = "out.png"
output_text_filename = "out.txt"
from lib import *
def double_range(limit1, limit2): #y - x
  """Produce all pairs in (0..`limit1`-1, 0..`limit2`-1)"""
  for i1 in range(limit1):
      for i2 in range(limit2):
          yield i1, i2

from PIL import Image, ImageDraw

print("--PROCCES STARTED")

img = Image.open(image_filename)

print("#image loaded")

x=0
y=0

bin_data= []
temp_word = ""

for y, x in double_range(img.height, img.width):

  pixel = img.getpixel((x, y))
  # print(x, "-", y, pixel)
  temp_word += str(255 - pixel[3])
  # print(len(temp_word))
  if len(temp_word) == 7 :
      # print("lol")
      if temp_word == "0000000" : break
      bin_data.append(temp_word)
      temp_word = ""

print("#algorithm done")

file = open(output_text_filename, 'w')
print("#txt opened")
print(bin_data)
for i in bin_data:
  file.write(search(i, "bin>str"))

print("#txt write done")
print("--PROCCES FINISHED")
