#Name:  elise harris
#Date:  feb 6, 2019
#This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has no green channel.

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

imagename=input("Enter name of the input file: ")
img=plt.imread(imagename)
namegiven=input("Enter name of the output file: ")

plt.imshow(img)		           #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0
#img2[:,:,2] = 0          #Set the blue channel to 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()               #Show the image (waits until closed to continue)

plt.imsave(namegiven, img2)  #Save the image we created to the file: namegiven
