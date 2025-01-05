#W2 L2
#Wite a python program whivh will subtract the following values '40.5' and "20"

a = "40.5"
b = "20"
c= float(a)
d= int(b)
print('The substration is',c-d)

#syntax error = spelling,variable name , indentation
#logic error = getiing diferrent no. the below here is its example
a= 45
b= 73
c= 82
d= a+b+c/3 # mistake here we have to put () to do addition first eg d= (a+b+c)/3
print ('the average is', d)

#class exercise slide 37
a= "Eric Idle"
b= "Eric*1934"
print('Welcome', a ,'!')
print('The registration is complete.')
print('Your Temporary password:', b)
 
k= int(input("Enter a number")) #integer as an input
l= float(input("Enter a number")) #float as an input
m= str(input("Enter a string"))  #string as an input
print (k)
print (l)
print (m)

a,b,c=25,78,12
print(a)
print(b)
print(c)

#39 Class ex = Write a python program that assign 3 tax amounts to 3 variables all in one statement. Then print all the values using one print 
# statement with the sep keyword. 

a,b,c=25,19,21
print(a,b,c , sep=',') 
 
#38 Class  EX. Calculate the sum using explicit continuation \
grade1= 62
grade2= 32
grade3= 52
grade4= 43
sum=(grade1+\
        grade2+\
            grade3 +\
                grade4)

print("the value is",sum , end='*')

#54 Ex. Create a program that calculates a user’s weekly gross and take-home pay.
a=int(input('Hours worked'))
b=float(input('Hourly pay rate'))
taxrate=18
grosspay= a*b
taxamount= grosspay*(taxrate/100)
takehomepay=grosspay-taxamount
print('Pay check calculator')
print('Hours Worked :', a)
print("Hourly Pay Rate : ", b)
print("Gross Pay : ",grosspay)
print("Tax Rate : ",taxrate , '%')
print("Tax amount : ", taxamount)
print("Take Home Pay : ",takehomepay)


# NOTE We use import math function to us math library with mathamatical built-in functions
import math as m
b=m.sqrt(25)
print(b)
c=m.pow(3,5)
print(c)

#Ex Write a python program to print the area of a circle
import math as m
r=float(input("Enter the radius of circle"))
c=m.pi*m.pow(r,2)
print('The area of traingle',c) 

#Round function is used to round up decimals 
d= 4.14829
x = round(d,2)
y = round(d,3)
print(x)
print(y)
