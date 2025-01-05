#w5 L1
#conditional statement

l1="my name is Agam"
l2="my name is Agam"
if(l1==l2):
  print("two strings are equal")
else:
   print("two strings are not equal")

l1="my name is agam"
l2="my name is "
if(l1>l2): #this consider order of alphabets as bigger for last ale greater like z and a is smmaler
   print("strings 1 is greater than string 2")       
else:
    print("string 1 is less than string 2")
 
#Nested if statement

s1 = 45
s2 = 65
sum = s1 + s2
multipy = s1*s2
if (sum>100):   #we have to take care of indentation
    print(sum)
    if (multipy>100):
        print ("The vaue is", multipy)
    
s1 = "123456"
if(s1.isdigit()):
    s2 = int(s1)
    if(s2>1000):
        print("The result is", s2)
else:
    print("This is not a digit")
    
# .isalpha function check if a variable contains alphabet    
f1="python"
if(f1.isalpha()):
    f2="programming"
    f3=f1+f2
    print (f3)
    if (f3=="pythonProgramming"):
        print(f3)
else:
    print("The string does not contain any alphabets")   
    
#Write a python program which will check whether a string is im lower case. If the string is in lowercase, then it will check whether
#it contains spaces or not.If it contains spaces then print string otherwise print no string 
  
a = " hello world "
if(a.islower()):
    if(a.isspace): #it is not working coz of glitch so we preffer M2 
        print("Space")
    else:
        print("No Space") 

#M2
a = "helloworld"
if(a.islower()): #m2 is not considering lowercase
    if ' ' in a:
        print("Space")
    else:
        print("No Space")
        
# List 
x1 = [12 , 10 , 21 , 72 , 62]  
print(x1)
x2 = [62 , 7 , 101 , 201.25 , 15.755 , "hello" , "kida oye"]
print(x2)
#nested list (list inside another list)
x3 = [24 , 9 , 34 ,["spam" , 1.298 , "Basketball" , "LBJ"]]
print(x3)

#Indexing - we can also use indexing in list
l = [1 , 2 , "Hi" , 8.7 , "Agam"]
print(l[1])
print(l[2],l[4])
#Slicing - In list, you can aslo do slicicing to print a portion of list
print(l[3:5])

#Write a python programm which will create a list that will have the following values: 45,93,140,150.67,89.358,"Python","Programming",
# "My","Name"['spam',45.67,95]. Then it will print the values "python",Programming","My" and "Name".
f = [45,93,['spam',45.67,95]]
print(f[1:3])
print(f[2])
print(f[2][0]) #to print specific word inside/from a list which is already iin list eg^^