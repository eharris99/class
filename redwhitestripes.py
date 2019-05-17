#Name:  elise harris
#Date:  feb 15, 2019
#assignment 18, red and white stripes


#Import the libraries for arrays and displaying images:
import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)

stripenum=input("Enter the size: ")
stripenumint=int(stripenum)
filename=input("Enter output file: ")

stripesImg = np.zeros((stripenumint,stripenumint,3)) #stripenumint array with 3 sheets of zeros
#print(stripesImg)
stripesImg[:,:,0]=1
stripesImg[:,:,1]=1
stripesImg[:,:,2]=1

stripesImg[::2,:,1:]=0

#stripesImg[slice(0,stripenumint,2),:,1]=0
#stripesImg[slice(0,stripenumint,2),:,2]=0
 

#Load the stripes image into matplotlib.pyplot:
plt.imshow(stripesImg)
#plt.imsave("stripesimage.png", stripesImg) #Save the image to .png
#show the stripes image to confirm it looks right
plt.show()

plt.imsave(filename, stripesImg) #Save the image to filename

#stripesImg[::2,:,1:]=0


