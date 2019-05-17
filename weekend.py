#Name:  elise harris
#Date:  feb 14, 2019
#assignment 19, weekend

#1.  Ask the user for the number of hours until the weekend.
#2.  Print out the days until the weekend (days = hours // 24)
#3.  Print out the leftover hours (leftover = hours % 24)


numhours=input("Enter number of hours: ")
days=int(numhours)//24
print("Days: " + str(days))
leftover=int(numhours)%24
print("Hours: " + str(leftover))
