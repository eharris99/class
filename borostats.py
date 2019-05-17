#Name:  elise harris
#Date:  Feb 28, 2019
#Program #28: borough stats

import matplotlib.pyplot as plt
import pandas as pd

borough=input("Enter borough: ")

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

boroavg=pop[borough].mean()
boromax=pop[borough].max()

print("Average population: ",boroavg)
print("Maximum population: ",boromax)
