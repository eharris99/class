#Name:  elise harris
#Date:  Feb 28, 2019
#Program #31: greetings by the hour


timestr=input("Enter hour (in 24 hour time): ")
time=int(timestr)

if (time < 12):
    print("Good Morning")
elif ((time >=12) and (time <17)):
    print("Good Afternoon")
else:
    print("Good Evening")
