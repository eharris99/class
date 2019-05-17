#Elise Harris
#March 19, 2019
#collisions location 

#Import pandas for reading and analyzing CSV data:
import pandas as pd

collisions = pd.read_csv('NYPD_Motor_Vehicle_Collisions.csv') #Name of the CSV file
latlong=input("Enter latitude and longitude: ")
print(collisions.head())
print(collisions["LOCATION"].value_counts()[:10])
