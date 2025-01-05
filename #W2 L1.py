#W2 L-1
print('"I am going for a walk" , "lunch"' , sep=',') 
print("'I will attend the class' , 'Lunch'" , sep=',')
print('"My name is Agambir Singh | 18772871"', sep="|")

#We can only use one sep here 
print ('I will eat,watch movies? sleep' , sep=',')
print('I will eat', 'watch movies? sleep', sep=',')

#We can direlty do calculation in python using print function
print(76+24)
print('The resullt is',20/10)
print(7*7.8)

#to convert a number eg5 into string we use type casting/conversion
a= 5 
b= str(a)
print(type(b))
c=float(a)
print(type(c))
print(c)

#if we want to print 5 like "5" then we use f which means format
print('" "',b) #it will not work
print(f'"{b}"')

# Write a program which take an integerz value,convert it to a str
a= 21
b=(str(a))
print(f'"{b}"')


