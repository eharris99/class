#Name:  elise harris
#Date:  Feb 27, 2019
#Program #27: borough pop

import matplotlib.pyplot as plt

import pandas as pd

borough=input("Enter borough name: ")
output=input("Enter output file name: ")
pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop['Fraction'] =pop[borough]/pop['Total']
pop.plot(x="Year", y="Fraction" )

plt.show()

fig = plt.gcf()
fig.savefig(output)
