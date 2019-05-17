#Elise Harris
#March 11, 2019
#parking tickets attribute

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
attribute=input('Enter attribute: ')
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10]) #Print out the dataframe
