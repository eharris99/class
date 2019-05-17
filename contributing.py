#Elise Harris
#March 13, 2019
#parking tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
offenders = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("Top three contributing factors for collisions:")
print(offenders["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
#Print out the dataframe
