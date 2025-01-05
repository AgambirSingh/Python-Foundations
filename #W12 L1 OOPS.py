#W12 L1 OOPS
class car:
    def __init__(self,model,maker,colour,type,year): #__init__constructor to assign values
        self.model=model
        self.maker=maker
        self.colour=colour
        self.type=type
        self.year=year
    def print(self):
        print("the car mdoel is",self.model)
        print("The maker of the car is", self.maker)
        print("The colour of the car is", self.colour)
        print("The type of the car is", self.type)
        print("The year of the car is", self.year)
#car1 is an object of the class car that has the above properties
#model= "Toyota Crown", Maker="Toyota" etc...
car1=car("Toyota Crown","Toyota","Black","Manual",2020) 
car2=car("BMW I35","BMW","White","Automatic",2004)
print(car1.colour) #it will print the colour member from the object car 1
print(car2.model) #it will print the model member from the object car 2
car1.print() #it will access the print function for the object car1
print()
car2.print() #it will access the print function for the object car2


#pig dice game from exercise
file=open("rules.txt","w")
file.write("Pig Dice Rules:\n")
file.write("See how many turns it takes you to get 20.\n")
file.write("Turn ends when player rolls a 1 or choose to hold.\n")
file.write("If you roll a 1 , you lose all points earned during the turn\n")
file.write("If u hold, you save all points eaned during the turn\n")
file.close()
with open("rules.txt") as file:
    content=file.read()
    print(content)
with open("rules.txt") as file:
    content=file.readlines()
    print(content)
with open("rules.txt") as file:
    for line in file:
        lines=line.split()
        print(lines)
with open("rules.txt") as file:
    for line in file:
        if line.startswith("Turn"):
            print(line)
with open("rules.txt") as file:
    for line in file:
        if line.endswith("turn\n"):
            print(line)
with open("rules.txt") as file:
    for line in file:
        if line.find("points")==-1:
            continue
        print(line)
counter_lines=0
counter_words=0
with open("rules.txt") as file:
    for line in file:
        counter_lines+=1
        counter_words+=len(line.split())
    print(counter_lines)
    print(counter_words)
