#W3 L1

x,y,z=10,20,30
x+=75 #it means x=x+75 they are called assigned compounds
print(x)
y*=2
print(y)

#Write a python program which will take inputs from the user. The inputs will be strings and you will convert the strings to integer and float 
# numbers andthen you wil add 100 to integers input and multiply 5 to the float input. Round the output of the float varibale to 2 decimals.
# Use coumpound assignments

a=input('Enter a number')
b=input('Enter another float number')
a=int(a)
b=float(b)
a+=100
b*=5
 
print(a)
print(round(b,2))

# Adding two strings
k="My name is Agam."
l="I like to play basketball"
m= k + l
print(m)

# Multiplying strings
g="I like reading"
h= g*5
print (h)

# Ex.Write a programm to get ouput 5 times
x="My name is Agambir"
y="My student id is 99999"
z="My course name is CST-SDNE"
i="My class section is 0000"
g=x*5,y*5,z*5,i*5
print(g)

#Enter two inputs in single line
a,b=input("Enter two numbers").split() #we can either use split like .split() or if we use , in .split(',') then we enter , to seprate two numbers in output
a,b=(float(a),float(b))
print("The sum of the numbers",a+b)

#INDEXING  - Used to print any individual letter of a string using third bracket

x= "My name is Agambir"
print(x[0]) # index always start from 0 thatswhy INDEX NUMBERS = len(string)-1
print(x[2]) #it also include space as character 
print(len(x)) #to find length of string we use print(len(x))

x= "I like football"
print(x[2:6])
# string index-means location of particular bit [start index : last index + 1]  
print(x[7:15])
print(len(x)) #len fn. gives length
#STRING SLICING-it will print letters btw 2 and 6
print(x[:7])
print(x[2:])

#Write a python program which will print the following words from the string below
x=("I am attending the class")
print(x[2:4])
print(x[5:14])
print(x[19:])
print(x[:4])
print(x[5:])
