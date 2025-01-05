#W14 practice
import math as m
def Area_perameter (r):
    Area=m.pi*(r*r)
    Perimeter=2*m.pi*(r*r)
    print("Circle: ",Area,":",Perimeter)    
b=int(input("Enter the number of circle :"))
counter=0
for i in range(1,b+1):
    i=int(input("Enter the radius: "))
    print(Area_perameter(i))

#using while loop
i=0
num=int(input("Enter the number of circle :"))
while i<num:
    radius=float(input("Enter the Radius value"))
    Area=m.pi*radius

#Guess number
import random #Import the random module to generate random numbers
num = random.randint(1,100) #Generate a random integer between 1 and 100 and assign it to the variable "number"
print("Guess a number between 1 and 100") #Using print statement to prompt user to guess a number 
while True: #Using While loop to create an infinite loop to repeatedly ask the user for guessing the number
    guess_num = input() #Get input from user and store the value in guess_num variable
    i = int(guess_num) # Convert the user's input (which is a string) to an integer and store it in the variable "i"
    if i == num: # Check if the user's guess matches the randomly generated number
        print("You Won") # If the guess matches the number, print "You Won" and break out of the loop
        break
    elif i < num:# If the guess is lower than the number, print "Too Low"
        print("Too Low")
    elif i > num:# If the guess is higher than the number, print "Too High"
        print("Too High")
