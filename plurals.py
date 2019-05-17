#Name:  elise harris
#Date:  feb 26, 2019
#plurals

array =input("Please input a list of nouns: ")
newarray=array.split(" ")
arraylength=len(newarray)
plurals=[]

#print(array)
for i in range(0,arraylength):
    #print(arraylength)
    if newarray[i][-1]=="s":
        print(newarray[i])
        plurals+=newarray[i]

#print(plurals)
