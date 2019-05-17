#Name:  Elise Harris
#Date: January 31, 2019
#This program prints ascii

mess=input('Enter a phrase: ')
print("In ASCII: ")
for j in range(0,len(mess)):
    print(ord(mess[j]))
