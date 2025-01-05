#W10 L2 Cont.-Function
#last class recap
#prog-Write a python programm which will program the following
# i) a function that will print "python" from the string "python programming" and then print each letter from the word "python" using loop 
# ii) A function that will add all the digits from an integer input for example- 1+2+3+4+5=15

def string_slicing(p):
    a=p[0:6]
    print(a)
    for i in a:
        print(i)
    return(i)

string="python programming"
print(string_slicing(string))

def add_digits(g):
    str_digit=str(g)
    sum=0
    for k in str_digit:
        int_digit=int(k)
        sum+=int_digit
        print(int_digit,"+ ",end="")
    print(" =",sum)
    return(sum)

digits=int(input("Enter an integer: "))
print(add_digits(digits))

#Prof method for ii)
def adddigit(n):
    sum=0
    while n>0:
        digit1=n%10 #we are separating the digits
        sum=sum+digit1
        n=n//10
    return (sum)
n=int(input("Enter an integer: "))
print(adddigit(n))

#TUPLE-It uses () bracket and act as a list

#Code the determines the count of passing grades (must be greater than 50 to pass)
# def processGrades (grades):
#     countPassing = 0
#     for grade in grades:
#         if grade > 50:
#             countPassing +=1
#             return countPassing
# def main():
#     grades=(45, 90, 87, 8, 88, 71) #This is tuple
#     countPassing=processGrades(grades) # creating a tuple of grades
#     print("the count of passing grades is {}: ".format(countPassing))
# if __name__=="__main__": #if this module is the main module
#     main() #call the main() function

#tuple
# a = (45, 67, 89, 93, 24)
# a[0]=92 # This will give you an error since tuple is immutable
#         #You can not change values in a tuple 
# print(a)
a = [45, 67, 89, 93, 24]
a[0] = 48 
print(a)
b= (45, 67, 89, 93, 24)
c=list(b) # The list() function will change the tuple to a list 
print(c)


#PROG- it calculates the average of passing grades for grades entered by a user; #passing grades must be >= 50 and grade <= 100.
def processGrades2(grades_count):
    count = 0
    countPassing = 0
    theSum = 0
    while count < grades_count:
        grade = float(input("Enter a grade: "))
        if grade > 50 and grade <= 100:
            theSum += grade
            countPassing +=1
        count +=1
    return theSum, countPassing
def main1():
    grades_count = int(input("Enter the number of grades: "))
    passing = processGrades2(grades_count)
    average = passing[0]/passing[1]
    print ('The average of the passing grades is {}'.format(average))
        
if __name__== "__main__": # if this module is the main module
    main1() # call the main() function
    
# BUBBLE SORT - It compares index value of elements in a list, and the smallest value will go forward
def bubblesort(list):

    for iternum in range(len(list)):
        for idx in range(len(list)-iternum-1):
            if list[idx]>list[idx+1]:
                temp=list[idx] #Storing the value 19 to the temp variable
                list[idx]=list[idx+1]#it will move to the index position of 2 since it's the smallest
                list[idx+1]=temp #2 will move to the index position of 19
def main():
    list=[19,2,31,45,6,11,121,27]
    bubblesort(list)
    print(list)
if __name__=="__main__":
    main()

# BINARY SEARCH- we divide the list in 2 portions (refers to notes detailed explanation)
def binary_search(arr, x):
    low = 0  # Initialize the lower bound of the search range
    high = len(arr) - 1  # Initialize the upper bound of the search range

    while low <= high:  # Continue until the search range is valid
        mid = (high + low) // 2  # Calculate the middle index

        if arr[mid] < x:  # If value at mid is less than x, ignore left half
            low = mid + 1
        elif arr[mid] > x:  # If value at mid is greater than x, ignore right half
            high = mid - 1
        else:  # If value at mid equals x, we found the target
            return mid

    # If x is not found, return -1
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Call the binary search function
result = binary_search(arr, x)

if result != -1:
    print(f"Element {x} is present at index {result}.")
else:
    print(f"Element {x} is not found in the array.")