#W11 L1 
# Files
file=open("testfile.txt","w")
file.write("I am attending python course\n")
file.close()
with open("testfile.txt","w") as file:
    file.write("My name is Agambir Singh\n")
with open("testfile.txt","a") as file:#a means append-to add
    file.write("I am attending python course 2")

# IT WILL READ CONTENT FROM THE FILE
with open("testfile.txt") as file:
    content=file.read()
    print(content)
    
with open ("testfile.txt") as file:
    for lines in file: #Loop through the contents from the file
        print(lines)
        
with open("testfile.txt") as file:
    content=file.readlines()#it will convert the content of files into list
    print(content) # it will print the contwnt of the file as list
    print(content[0])

with open("testfile.txt") as file:
    for line in file:
        content=line.split() #split each word from a line and turn it into list
        print(content) 

#Prog-
#1) Create a file named pythonfile and write the following; I am attending python course , I am learning file
#2) Append the following line to the file "I am also learning binary search algorithm"
#3) Print the total number of lines in the file
#4) print the following words from puthon the file: python course, file , binary search

file=open("pythonfile.txt","w")
file.write("I am attending python course I am learning file\n")
with open("pythonfile.txt","a") as file:
    file.write("I am also learning binary search algorithm\n")
with open("pythonfile.txt") as file:
    content=file.readline()
    print(content[14:28])
    print(content[42:47])
    print(content[65:79])
count=0
with open("pythonfile.txt") as file:
    for lines in file:
        count+=1
print(count)    