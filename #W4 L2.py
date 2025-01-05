#W4 L2
assignment = float (input ("What grade did you get for the assignment?: "))
quiz = float (input ("What grade did you get for the quiz?: "))
mid_term = float(input ("What grade did you get for the mid-term?: "))
exam = float (input ("What grade did you get for the final?: "))

total_grade = assignment*0.25 + quiz*0.10 + mid_term*0.30 + exam*0.35
if 100 >= total_grade >= 95:
    print("You got an A+")
elif 95 >= total_grade >= 90:
    print("You got an A")
elif 90 >= total_grade >= 85:
    print("You got an A-")
elif 85 >= total_grade >= 80:
    print("You got a B+")
elif 80 >= total_grade >= 75:
    print("You got a B")
elif 75 >= total_grade >= 70:
    print("You got a C")
elif 70 >= total_grade >= 50:
    print ("You got a D")
else:
    print ("You got a F")
    
#prof 1
q=float(input("Enter your quiz number"))
if(q>=18):
    print("Your grade is A")
elif(q>=16 and q<18):
    print("Your grade is B")
elif(q>=14 and q<16):
    print("Your grade is C")
elif(q>=12 and q<14):
    print("Your grade is D")
else:
    print("Your grade is F")
    
#prof 2
custtype= input("Enter customer type")
purchase= int(input("Enter total purchase"))
if(custtype=='r'):
    if(purchase>0 and purchase<100):
        discount=0.1
        discountpercent=0.1*100
        discountedamount=purchase*discount
        Total=purchase-discountedamount
        print("Price before discount is", purchase)
        print("Discount percent is", discountpercent)
        print("discountedamount is", discountedamount)
        print("Price after discount is", Total)