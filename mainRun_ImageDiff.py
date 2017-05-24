#philosophicalMeerkat , Date late edited: 3/22/2017 , Challenge 3, Resources used: Lecture 9, https://blackboard.olemiss.edu/bbcswebdav/pid-407955-dt-content-rid-2031586_1/courses/Csci_343_Section_1_JONES_2016-2017_SPRG/Lecture_9_web.pdf
#Pillow improved image library, How to show two figures using matplotlib? http://stackoverflow.com/questions/7744697/how-to-show-two-figures-using-matplotlib

#!/usr/bin/python
from __future__ import division
from PIL import Image
#from PIL import Image #some of you might to use this line to import the Image library
import matplotlib.pyplot as mplot #imports MatPlotLib
import numpy as np #imports NumPy
import os #imports OS tools
#reads list of files from the directory "your_images"
files=os.listdir("einsteinatanderson")
avg_img=[0,0,0] #Holds average image
stnd_dev=[0,0,0] #Holds Standard Deviation
image_list = []

w,h = Image.open("einsteinatanderson/"+files[0]).size
threshold = raw_input("Please enter a threshold: ") 

print(threshold)
#loops though all files listed in your directory
for i in range(0, len(files)):
#if the file is a jpg image...
    if ".jpg" in files[i]:
        #opens image file
        img=Image.open("einsteinatanderson/"+files[i])
        #converts image to a Float32 to do our math ops
        img=np.float32(img)
        image_list.append(img)
        avg_img += img #Summation for average
        
avg_img= avg_img/len(files) #Division calculation

#calculate standard deviation
for i in range(0, len(image_list)):
    stnd_dev += (image_list[i]-avg_img)*(image_list[i]-avg_img)

stnd_dev = (stnd_dev/len(image_list))**(.5)
#print(stnd_dev.__getitem__(0).__getitem__(0).__getitem__(0))

#loops through and changes pixels to red if the standard deviation is above the threshold 
for x in range(0, h): 
    for y in range(0, w):
        if sum(stnd_dev[x][y]) >float(threshold):
            avg_img[x][y] = [255.0, 0.0, 0.0]

#print(avg_img)

#clips pixel colors to between 0 and 255
avg_img=avg_img.clip(0, 255)
stnd_dev=stnd_dev.clip(0, 255)
#converts image back to unsigned 8-bit integer
avg_img=np.uint8(avg_img)
stnd_dev=np.uint8(stnd_dev)


#print(avg_img)
#displays images with MatPlotLib
#shows avergae image with area of difference coloered red
mplot.figure(1)
mplot.imshow(avg_img)
#shows standard deviation image
mplot.figure(2)
mplot.imshow(stnd_dev)
mplot.show()


