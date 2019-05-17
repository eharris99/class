#Name:  elise harris
#Date:  feb 28, 2019
#shelters

import pandas as pd
import matplotlib.pyplot as plt

datatouse=input("Enter name of input file: ")
output=input("Enter name of output file: ")
##homeless = pd.read_csv("DHS_Daily_Report.csv",skiprows=5)
##homeless.plot(x = "Date of Census", y = "Total Children in Shelter")


homeless = pd.read_csv(datatouse)
homeless["Fraction Children"]=homeless["Total Children in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")
plt.show()

fig = plt.gcf()
fig.savefig(output)
