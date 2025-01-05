#w4 L1
# We use {in} fuction to compare two sentences
a=input("Enter the sentence")
b="My name is Agambir"
print (a in b) #matches the whole whole string with b

a="My name is Agambir"
b="I am going to walk"
c="Agambir"
print (a in b)
print(c in a)
print(a[5] in b[3])
print(a[3] in b[3])

# "is" - used to to check any condition
a="12345"
b= a.isdigit() # to check if value a is all digits
print(b)

#To check if every character in a string is  lowercase/UPPERCASE
a="i am agam"
b=a.islower()
print(b)
c="I AM AGAM"
d= c.isupper()
print(d)

# To change a whole variable in uppercase or lower case we use .upper() 
a="i am agam"
print(a.upper())

#Apply string slicing to taker the letter M and then convert it to lowercase
b="My name is Agambir"
c=(b[:1])
d=c.lower()
print (d)
#or in just 1 step
print(b[:1].lower())

#Format-Used to add a value/string to another statement 
name= input("Enter your name")
greeting= "Hello,{}!".format(name)
print(greeting)

a=input("name")
b="Hi {} ,How are you?".format(a)
print(b)


instructor=input("Enter the prof's name")
subject=input("Enter the subject name ")
term=input("Enter the term")
print("In term{2}, Professor{0} will teach {1}".format (instructor,subject,term))
print("In {0} semester, Professor {1} will teach {2}".format(term,instructor,subject))

#ex 
a=input("Enter your name")
b=input("Enter your student Id")
c=input("Enter your couse name")
print("My name is {0}. My student id is {1}. I am taking {2}".format(a,b,c))

#We can use formating to round a number
a=2.1976
b="the number is {:.2f}".format(a)
print (b)

#Conditional Statement 
#Conditional operators to be used with if,else,elfe
# == Equal
# != not equal
# > grater than >= greater than or equal
# < lesser than <= Lesser than or equal

#Prog-FIND if x is even or odd 
x=int(input("Enter number"))
if(x%2==0):
    print("Number is even")
else:
    print("Number is Odd")
    
    
