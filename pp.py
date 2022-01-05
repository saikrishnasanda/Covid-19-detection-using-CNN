from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk, Image
import cv2
import os
import sys
from tkinter import *
import tkinter as ttk
import random
import numpy as np
from playsound import playsound
from tkinter.filedialog import askopenfilename
import shutil
import PIL.Image
import matplotlib.pyplot as plt
   

root = Tk()

root.title("covid Prediction")

root.geometry("1280x720")
#root.configure(background ="LightCyan3")
BG = PhotoImage(file = 'red.png')
label = ttk.Label(root, image = BG)



dirPath = "testpicture"
fileList = os.listdir(dirPath)
for fileName in fileList:
    os.remove(dirPath + "/" + fileName)
# C:/Users/sagpa/Downloads/images is the location of the image which you want to test..... you can change it according to the image location you have  
fileName = askopenfilename(initialdir='C:\\Users\\Sush\\Desktop\\covid\\test', title='Select image for analysis ',
                       filetypes=[('image files', '.png')])
dst = "testpicture"
print(fileName)
print (os.path.split(fileName)[-1])
if os.path.split(fileName)[-1].split('.') == 'h (1)':
    print('dfdffffffffffffff')
shutil.copy(fileName, dst)
load = PIL.Image.open(fileName)


img = cv2.imread(fileName)
kernel = np.ones((6,6),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Preproccessed')

plt.xticks([]), plt.yticks([])
plt.show()
playsound("pp.mp3")


