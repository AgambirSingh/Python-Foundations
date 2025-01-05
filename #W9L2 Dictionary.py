#W9L2 Dictionary

countries={"CA":"Canada","US":"United States","IN":"India"}
print("countries:", countries)
print()#this will not print the desired result

search= countries.get("CA")#we use this command to use dictionary
print (search)
print(countries.get("IN"))
s=countries.get("US")
print(s)
s1=countries.get("UK","not found")
print(s1)
countries["UK"]="United kingdom"
print(countries)
for i,j in countries.items():
    print("%10s%20s"%(i,j))
#Empty Dictinary--it does not have any limit so we can add unlimited values to it
D ={} 
D["CA" ]="Canada"
D["python"]=12456
print(D.get("python"))

fruits={}
fruits["banana"]=4092
fruits["apple"]=4042
for fruit, code in fruits.items():
    print("%10s%20s"%(fruit, code)) #to add space in print statement we us %10s where s mean space 
del fruits["apple"]
print(fruits)

#prog Slide 37 w9 
#Tuples and Dictionaries: Do it yourself !
#• Write a python program to check if a course code is in the dictionary courses before deleting it; if
#so, it will be deleted and a message (‘ The course is deleted.’) is displayed to the user; otherwise, a
#message (‘ There is no course for this code’) is displayed.
#• The program starts with an empty courses dictionary and a few items are added later.
#• It prompts the user to enter a code to check for.

course={}

course["CS120"]= "iNTRODUCTION TO COMPUTER SICENE"
course["MATHS07"]="Maths"
course["COMM182"]="Communication"
code= input("Enter your couse code")

if code in course:
    del course[code]
    print("The course is deleted")
else:
    print("There is no course for this code")
print(course)
    
#Tuples and Dictionaries: Do it yourself !
#• Create two Python dictionaries: English to Spanish and Spanish to German. Use
#online dictionaries on the internet to build these dictionaries of a few items in each.
#• Write code that prompts the user to enter a word in English then your program
#should translate it into German using the two dictionaries you built.

english_to_spanish={
    "hello":"hola",
    "goodbye":"adios",
    "thank you":"gracias",
    "please":"por favor"
}

spanish_to_german ={
    "hola":"hallo",
    "adios":"auf Widersehen"
}

word=input("Enter a word in english")

#Translate the word from English to spanish
if word in english_to_spanish:
    spanis_word=english_to_spanish[word]
    #Translate the word from spanish to german
    if spanis_word in spanish_to_german:
        german_word=spanish_to_german[spanis_word]
        print(f"The German Translation of '{word}' is {german_word} ")
    else:
        print("Translation in German not Found")
        
#Break and .split function
string, letter=input("Enter the string the letter you ar elooking for").split() #to take two input
for l in string:
    if letter==l:
        print("the index of "+l+"is",string.index(l))
        break #it mannually exit from the loop after it found the result
              #so the programm exit from getting into infinite loop
else:
    print("The letter is not not in string")
    
#write a python prog which will look for largest and smallest value in a list using for loop
List=[21,34,9,99,34,62]
for i in List:
    print(min(List))
    print(max(List))
    break


    
    
