#Name:  elise harris
#Date:  feb 14, 2019
#assignment 18, red and white stripes

import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)

logoImg = np.ones((10,10,3)) #10x10 array with 3 sheets of 1’s
#Load the array into matplotlib.pyplot:
plt.imshow(logoImg)
#Display the plot:

##2 Set the 3 left columns to be purple.
##To make purple, we’ll keep red and blue at 100% and turn green to 0%
logoImg[:,:3,1] = 0 #Turn the green to 0 for first 3 columns
logoImg[4:6,:,1] = 0
logoImg[:,7:10,1] = 0

##3 Set the 3 right columns to be purple.

plt.imshow(logoImg)
plt.show()
##4 Set the middle 2 rows to be purple.
#logoImg[:,:,1] = 0 #Turn the green to 0 for middle rows

##5 Save logo array to file.
plt.imsave("logo.png", logoImg) #Save the image to logo.png



