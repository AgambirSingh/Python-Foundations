#W9 L1 continuation of foreloop
#To iterete through list of values
i = [21,62,41.5,90.5]
for x in i:
    print(x)
for y in [61,82,34,56,54]:
    print(y)
    
#list comprehension    
n=[i for i in [22,32,45,65,32]] #we do not use semicolon here
print(n)

#to print only odd values  using list comprehension
k=[12,43,64,32,55,69]
n1=[i for i in k if i%2!=0]
print(n1)

for z in "apple":
    print(z)
#NOTE: we only use list comprehension to itereate through a list
# for z1 in 12: #we cannot use for loop for only 1 valuw
#  print(z1)
 
for i in range(1,50):
    print(i)
    
#Write a python program which will count the total number of digits alpabets and special charactes in your input using for lopp

String = input("Enter an input: ")

digit=0
alpa=0
s=0
for i in String:
    if i.isalpha():
        alpa +=1
    elif i.isdigit():
        digit+=1
    else:
        s+=1 
print("Digit", digit)
print("Alphabet", alpa)
print("Special Character", s)

#NESTED FOR LOOOP
#print the the following pattern
#*
#**
#***
#****
#*****
for r in range(5):
    for c in range(r+1):
        print("*", end=" ")
    print()

#prog-
#*****
#******
#*******
#********

for i in range(5,9):
    for b in range(i+1):
        print("*", end="" )
    print()

#prog- to print average of 4 quizes and 5 assignments in your course
sumq=0
suma=0
count1=0
count2=0
for i in range (4):
    q= float(input("Enter quiz number"))
    sum1=sumq+q
    count1= count1+1
for o in range(5):
    p= float(input("Enter assignment number"))
    sum2=suma+p
    count2=count2+1
avg_q=sum1//count1
avg_asg=sum2/count2
print("Average of quiz number = ", avg_q)
print("Average of asssignment number = " , avg_asg)
