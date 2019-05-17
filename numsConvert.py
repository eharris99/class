#CSci 127 Teaching Staff
#March 11 2019 programming assignment 38
#A program that uses functions to print out integer names.
#Modified by:Elise Harris

def num2string(num):
     """
     Takes as input a number, num, and
     returns the corresponding name as a string.
     Examples: num2string(0) returns "zero", num2string(1) returns "one"
     Assumes that input is an integer ranging from 0 to 9
     """
     
     numString = ""
     
     numwords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
     #print(type(num))
          
     numString=numwords[num]      

     return(numString)


def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()
