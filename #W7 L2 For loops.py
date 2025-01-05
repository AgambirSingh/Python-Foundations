#W7 L2 For loops
#refer to notes for explanation
for i in range(1,11):
    print(i)
    
for b in range(1,101):
    print(b)

#
s="python programming"
for i in s:
    print(i)
    
#write python program which print out the string "python programming" 10 times
k="Python programming"
for i in range(1,11): #always use counter variable 
    print(k)
    
#prog-Compute factorial for any number

number=int(input("Enter a number"))
factorial=1
for i in range(factorial,number+1): #loop throught 1 and the number 
    factorial = factorial * i #it will compute factorial by multiplying 
print(factorial) 

#prog- Determine the prime number using for loop

number=int(input("Enter a number"))
prime=False
if number==1 and number==0:
    prime=True
elif number>1:
    for i in range(2,number):
        if (number%i==0):
            prime=True
if (prime):
    print (number," is not a prime number")
else:
    print(number," is a Prime number")

#prof method
number=int(input("Enter a number"))
flag=False
if number==1 and number==0:
    flag=True
elif number>1:
    for i in range(2,number):
        if(number%i==0):
            flag=True
if(flag):
    print(number,"is not a prime number") 
else:
    print(number,"is prime number")
    
#Count the number of variables in list

count=0
for i in [2,4,6,8,10,24]:  #We can also use list in for loop
    count=count+1
print(count)

#Continue keyword
for i in range(5,15):
    if i==6:
        continue #it skips value 6 due to the continue keyword
    else:
        print(i)