#W10 L1 Functions
#Built in functions= improrted fom library in python==>Pront, input function , min, max , sum , del , join oppend, .isdigit() etc.
#user define function= User create the function using def() keyword. It helps us to break down a bigger problem into smaller portions

#Prog- i)A function which decides if an input is odd or even 
#      ii)A function which decides the sum 1 to n(input)
#      iii)A function which decides to add the followong from the list {4,6,10,12,14,16}
def oddoreven(n): #dev variable or function name choose any random name(another variable)
    if(n%2==0):
        print("number is an even number")
    else:
        print("number is an odd number")
    return n #the result that we are trying to get , (not compulsary)

def sum(k):
    sum=0
    for i in range(1,k):
        sum+=i
    return sum

def addlist(j):
    sum1=0
    for i in j:
        sum1+=i
    return sum1
n=int(input("Enter an integer"))
oddoreven(n)

k=int(input("Enter an integer to take sum"))
print(sum(k))

j=[4,6,10,12,14,16]
print(addlist(j))

# When using functions in a program, you generally isolate each task within the program in its
# own function. For example, a realistic pay calculating program might have the following
# functions:
# • A function that gets the employee’s hourly pay rate
# • A function that gets the number of hours worked
# • A function that calculates the employee’s gross pay
# • A function that calculates the overtime pay
# • A function that calculates the withholdings for taxes and benefits
# • A function that calculates the net pay
# • A function that prints the paycheck

def hourly_payrate():
    hourly_payrate=float(input("Enter hourly pay rate: "))
    return(hourly_payrate)
def hours_wrk():
    hours_wrk=float(input("Enter number of hours worked: "))
    return (hours_wrk)
def gross_pay(hourly_payrate,hours_wrk):
    return hourly_payrate*hours_wrk
def calculte_ot(hourly_payrate,hours_wrk):
    if hours_wrk <=40:
        return hourly_payrate*hours_wrk
    else:
        regular_pay= hourly_payrate*40
        overtime_pay= (hours_wrk-40) * (hourly_payrate * 1.5)
        return regular_pay + overtime_pay
def cal_withholding(gross_pay):
    return(gross_pay*0.2)
def net_pay(gross_pay,cal_withholding):
   net_pay1=(gross_pay - cal_withholding)
   return net_pay1
def paycheck(net_pay1):
    print(f"Paycheck: $",net_pay1)

hp=hourly_payrate()
hw=hours_wrk()
gp=gross_pay(hp,hw)
co=calculte_ot(hp,hw)
cw=cal_withholding(gp)
np=net_pay(gp,cw)
pc=paycheck(np)


#prof method
# def get_hourly_pay_rate():
#             hourly_pay_rate = float(input("Enter employee's hourly pay rate: "))
#             return hourly_pay_rate
# def get_hours_worked():
#             hours_worked = float(input("Enter number of hours worked: "))
#             return hours_worked
# def give_gross_pay(hourly_pay_rate, hours_worked):
#       return hourly_pay_rate*hours_worked
# def calculate_overtime_pay(hourly_pay_rate, hours_worked):
#     if hours_worked <= 40:
#         return hourly_pay_rate * hours_worked
#     else:
#         regular_pay = hourly_pay_rate * 40
#         overtime_pay = (hours_worked - 40) * (hourly_pay_rate * 1.5)
#         return regular_pay + overtime_pay

# def calculate_withholdings(gross_pay):
#     # Example calculation for withholdings
#     return gross_pay * 0.2  # 20% withholding for taxes and benefits

# def calculate_net_pay(gross_pay, withholdings):
#     return gross_pay - withholdings

# def print_paycheck(net_pay):
#     print("Paycheck Details:")
#     print(f"Net Pay: ${net_pay:.2f}")

# hourly_pay_rate = get_hourly_pay_rate()
# hours_worked = get_hours_worked()
# gross_pay1 = calculate_overtime_pay(hourly_pay_rate,hours_worked)
# withholdings = calculate_withholdings(gross_pay1)
# net_pay = calculate_net_pay(gross_pay1, withholdings)
# print_paycheck(net_pay)