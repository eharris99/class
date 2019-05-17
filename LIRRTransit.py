#CSci 127 Teaching Staff
#March 2019
#A template for a program that computes LIRR transit fares.
#Modified by:  Elise Harris

def computeFare(z, t):     
    fare = 0
    if (z == 1 and t == "peak"):
        fare = 6.75
        
    if (z == 1 and t == "off-peak"):
        fare = 6.25
        
    if ((z == 2 or z == 3) and t == "peak"):
        fare = 10.25
        
    if ((z == 2 or z == 3)  and t == "off-peak"):
        fare = 5.75
        
    if (z == 4  and t == "peak"):
        fare = 12.00
        
    if (z == 4  and t == "off-peak"):
        fare = 8.75
        
    if ((z == 5 or z == 6 or z == 7)  and t == "peak"):
        fare = 13.50
       
    if ((z == 5 or z == 6 or z == 7)  and t == "off-peak"):
        fare = 9.75
    if (t=="senior"):
        fare = 4.5
        
    if z > 8:
        fare = -1
        
     
    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
