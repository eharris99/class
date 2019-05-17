#Name:  elise harris
#Date:  march 6, 2019
#quarter image


imagefilename=input("Enter image file name: ")
output=input("Enter output file: ")

#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread(imagefilename)   #Read in image
height=img.shape[0]
width=img.shape[1]
img2=img[:height//2, width//2:]

#Load the flood map image into matplotlib.pyplot:
plt.imshow(img2)

#Display the plot:
#plt.show()

#Save the image:
plt.imsave(output, img2)
