import tkinter as tk
from tkinter import filedialog, Text
import os
from lib import MAIN_WRITE
import time
from time import gmtime, strftime

def addImage():
    global image_filename
    image_filename = filedialog.askopenfilename(title="Select Image",
                                    filetypes= [("image", ".png .jpg .jpeg")])
    if image_filename == "" : exit()
    label = tk.Label(root, text = "Your input IMAGE is \n" + image_filename, height = 2);
    label.grid(row = 0, column = 1)

def addText():
    global text_filename
    text_filename = filedialog.askopenfilename(title="Select Image",
                                    filetypes= [("text", ".txt")])
    if text_filename == "" : exit()
    label = tk.Label(root, text = "Your input TEXT is \n" + text_filename, height = 2);
    label.grid(row = 1, column = 1)

def RUN():
    print(text_filename)
    print(image_filename)
    if (image_filename!="") and (text_filename!="") :
        # label = tk.Label(root, text = "WORKING", fg="#008800", width = 40, height = 2);
        # label.grid(row = 2, column = 1)
        # TODO: window frezes until procces is finished

        MAIN_WRITE(image_filename, text_filename,
        "IMG_OUTPUT " + strftime("%d_%m_%Y %H-%M-%S", gmtime()) + ".png")

        label = tk.Label(root, text = "DONE", fg="#008800", width = 40, height = 2);
        label.grid(row = 2, column = 1)
    else:
        label = tk.Label(root, text = "select image and text file, \n than press RUN again",
                            fg="#E71D36", width = 40, height = 2);
        label.grid(row = 2, column = 1)

root = tk.Tk()
root.resizable(False, False)
root.title("TXT to IMG")

image_filename = ""
text_filename = ""

addImage = tk.Button(root, text= "SELECT IMAGE FILE", padx=10, pady=5, fg="#011627",
                        bg = "#2EC4B6", command = addImage, width = 15)

addText = tk.Button(root, text= "SELECT TEXT FILE", padx=10, pady=5, fg="#011627",
                        bg = "#2EC4B6", command = addText, width = 15)

RUN = tk.Button(root, text= "RUN", padx=10, pady=5, fg="#FDFFFC",
                        bg = "#E71D36", command = RUN, width = 15)

label_image = tk.Label(root, text = "not selected", width = 20);
label_text = tk.Label(root, text = "not selected", width = 20);

label_image.grid(row = 0, column = 1)
label_text.grid(row = 1, column = 1)
addImage.grid(row = 0, column = 0)
addText.grid(row = 1, column = 0)
RUN.grid(row = 2, column = 0)

root.mainloop()
