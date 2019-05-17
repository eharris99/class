#Name:  elise harris
#Date:  march 6, 2019
#name organizer

list=str(input("Please enter your list of names: "))
#print(list)
list2=list.split("; ")
"".join(list2)
#print(list2)
for i in range(0,len(list2)):
    list2[i]=list2[i].split(", ")

print("You entered:")

for i in range(0,len(list2)):
    print(list2[i][1] + " " + list2[i][0])
print("Thank you for using my name organizer!")
