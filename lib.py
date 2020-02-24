def double_range(limit1, limit2): #y - x
    #Produce all pairs in (0..`limit1`-1, 0..`limit2`-1)
    for i1 in range(limit1):
        for i2 in range(limit2):
            yield i1, i2

def MAIN_WRITE(image_filename, text_filename, output_image_filename):
    from PIL import Image
    print("--PROCCES STARTED")

    # load files
    img = Image.open(image_filename)
    print("#image loaded")
    file = open(text_filename, 'r')
    print("#txt loaded")

    #read txt file
    input = file.read()
    bin_data = [] #array for binary data
    for i in input:
        bin_data.append(search(i, "str>bin")) #convert to binary
    print("#txt read done")

    # check img size
    if img.width*img.height < len(bin_data)*7 :
        print ("IMAGE TOO SMALL, CHOOSE BIGGER IMAGE")
        exit()
    print("#img size check done")

    # main algorithm
    x=0
    y=0
    alpha_channel = Image.new('L', img.size, 255) #create alpha layer
    for temp_word in bin_data :
        for i in temp_word:
            alpha_channel.putpixel((x,y), (255 - int(i))) # 255 if 0, 254 if 1
            x+=1
            if x == img.width :
                y+=1
                x=0

    img.putalpha(alpha_channel) #add alpha layer to img
    print("#algorithm done")

    img.save(output_image_filename)
    print("#img saved")
    print("--PROCCES FINISHED")

def MAIN_READ(image_filename, output_text_filename):
    from PIL import Image, ImageDraw
    print("--PROCCES STARTED")

    img = Image.open(image_filename)
    print("#image loaded")

    #main algorithm
    x=0
    y=0
    bin_data = [] #array for binary data
    temp_word = "" #binary data string for single char
    for y, x in double_range(img.height, img.width):
      pixel = img.getpixel((x, y))
      temp_word += str(255 - pixel[3]) # 0 if 255, 1 if 254
      if len(temp_word) == 7 : #when word is completed
          if temp_word == "0000000" : break #if there is no more user data
          bin_data.append(temp_word)
          temp_word = ""
    print("#algorithm done")

    file = open(output_text_filename, 'w')
    print("#txt opened")

    for i in bin_data:
        file.write(search(i, "bin>str")) #convert to binary
    print("#txt write done")

    print("--PROCCES FINISHED")

def search(word, mode):
    if mode == "bin>str" :
        return BIN_DICT[0][BIN_DICT[1].index(word)]
    if mode == "str>bin" :
        return BIN_DICT[1][BIN_DICT[0].index(word)]
    # TODO return empty str if no result found


"""
custom binary converter
"""
import string
zero = "0000000"
BIN_DICT = [["EOF"], [zero]] #first is End Of File char

for i in string.printable[:97]: #add all printable char
    BIN_DICT[0].append(i)

for num in range(1, 97+1): #increment binary number by one
    temp = str(bin(num))[2:] #convert to binary and delete "0b" prefix
    BIN_DICT[1].append((zero[len(temp):] + temp)[2:]) #this is shit is hard

BIN_DICT[1][0] = (BIN_DICT[1][0])[2:] #fix this in post




# print (search("-", "str>bin"))
