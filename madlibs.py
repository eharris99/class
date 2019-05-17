#Name:  elise harris
#Date:  feb 7, 2019
#assignment 17, mad libs


templateString = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."
noun=input("Enter a noun: ")
templateString = templateString.replace("NOUN", noun)
verb1=input("Enter a verb: ")
templateString = templateString.replace("VERB1", verb1)
verb2=input("Enter another verb: ")
templateString = templateString.replace("VERB2", verb2)
print("New sentence:")
print(templateString)
