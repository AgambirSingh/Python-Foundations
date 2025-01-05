#W11 L2 Files cont.

with open ("pythonfile.txt") as file:
    for lines in file:
        # .startswith it will look for the line in file that begin with thee word " I "
        if lines.startswith("I"):
            print(lines) # it will print the line that starts with word "I".

with open ("pythonfile.txt") as file:
    for lines in file:
        # it is looking for the line in file that end with with "algorithm"
        if lines.endswith("algorithm"):
            print(lines)
            
#.find() finding an alement put the f=value ==-1 it represent false
with open ("pythonfile.txt") as file:
    for lines in file:
        if lines.find("binary")==-1:# it is looking for lines that have pattern "binary"
            continue #skkiping the lines without pattern "binary"
        print(lines) #printing the line that has pattern "binary"
        
#Cannot add integers in file so we have to convert it
years=[1978,1947,1986]
with open("integerfile.txt","w") as file:
    for year in years:
        file.write(str(year)) # convert the elements into string data
with open ("integerfile.txt",) as file:
    content=file.readlines()
    print(content)
 