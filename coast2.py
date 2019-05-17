#Name:  elise harris
#Date:  Feb 27, 2019
#program 25: Takes elevation data of NYC and displays using the default color map


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
coast = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
            coast[row,col,0] = 0
            coast[row,col,1] = 0 
            coast[row,col,2] = .5     
        elif elevations[row,col] == 1:
            coast[row,col,0] = .75
            coast[row,col,1] = .75 
            coast[row,col,2] = .75
        else:
            coast[row,col,0] = .5
            coast[row,col,1] = .5 
            coast[row,col,2] = .5

#Load the flood map image into matplotlib.pyplot:
plt.imshow(coast)

#Display the plot:
#plt.show()

#Save the image:
plt.imsave('coast.png', coast)
