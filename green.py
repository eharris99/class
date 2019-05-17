#Elise Harris
#feb 4, 2019
#A program that demonstrates the shades of green

import turtle				#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")        #Make it turtle shaped
tess.backward(100)			#Move her backwards, to give more space to draw
#tess.color(0,128,0)

#For 0,10,20,...,250
for i in range(0,255,10):
     tess.forward(10)		#Move forward
     tess.pensize(i)		#Set the drawing size to be i (larger each time)
     tess.color(0,i,0)		#Set the red channel to be i (brighter each time)
