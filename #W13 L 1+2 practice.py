# W13 L1  practice
# uestion in w12 python exercise
# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included). The numbers
# obtained should be printed in a comma-separated sequence on a single line.
# For example: 2002, 2009, 2016, ...

for num in range(2000, 3201):
    if num%7==0 and num%5 !=0:
        print(num, end=",")
    
#2 Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without, hello, bag, world
# Then, the output should be:  bag, hello, without, world
L=input("Enter set ....").split(",")

List= input("Enter a set of words separataed by commas").split(",")
sort=sorted(List)
print(sort)
 
#3 Write a Python program that uses a loop to print the first 20 even numbers in descending order.

# even_numbers=[]
# for num in range(1,41):
#     if num % 2==0:
#         even_numbers.append(num)
# print(even_numbers[::-1])

#qs W13
#Define a function that takes as parameters, the total miles driven by a car and the miles driven per hours. The function calculates the estimated hours and minutes for a trip. 
#It prints the values of hours and minutes. In the main function, ask the user to enter the values of total miles and miles per hour, then call the defined function and pass both values
# def estimated_hrs(miles,mph):
#     print()
#     print("Travel Time Calcultaor")
#     est_hrs=miles/mph 
#     print(f"Hours: {int(est_hrs)}")
#     print (f"Minutes: {int((est_hrs % 1) * 60)} ")

# # Main function
# if __name__ == "__main__":
#     total_miles = float(input("Enter total miles: "))
#     miles_per_hour = float(input("Enter miles per hour: "))
#     estimated_hrs(total_miles, miles_per_hour)

# #2
# import random

# def check_guess(numbers):
#     guess = int(input("Enter a number to guess: "))
    
#     # Generate a random number from the list
#     random_number = random.choice(numbers)
    
#     # Check if the guessed number matches the random number
#     if guess in numbers:
#         return "LUCKY"
#     else:
#         return "UNLUCKY"

# def main():
# Create a list of 6 numbers
number_list = [1, 8, 4, 9, 16, 34]

# Call the function and pass the list
    result = check_guess(number_list)

    # Print out the returned result
    print("Result:", result)

# # Call the main function
# main()

# #3def add_contact(contacts):
# def add_contact(contacts):
#     name = input("Enter the name of the new contact: ")
#     phone = input("Enter the phone number of the new contact: ")
#     email = input("Enter the email of the new contact: ")

#     # Ask the user to select a manager
#     manager = int(input("Enter the manager index (0 for Karim, 1 for Lilly): "))
    
#     # Append the new contact to the selected manager's list
#     contacts[manager].append((name, phone, email))
    
#     # Return the updated list of contacts
#     return contacts

# def main():
#     # Create a list of two lists containing contacts of two managers
#     karim_contacts = [("Karim", "416 123 4567", "karim@abc.com")]
#     lilly_contacts = [("Lilly", "416 567 4321", "lilly@abc.com")]
#     manager_contacts = [karim_contacts, lilly_contacts]

#     # Call the function to add a new contact and pass the list of contacts
#     updated_contacts = add_contact(manager_contacts)

#     # Print out the updated list of contacts
#     for i, manager in enumerate(updated_contacts):
#         print(f"Manager {i}:")
#         for contact in manager:
#             print(contact)

# # Call the main function
# main()

#4
# def swap(param1, param2):
#     print("Before swapping:")
#     print("Parameter 1 is", param1)
#     print("Parameter 2 is", param2)

#     # Swap the values of the parameters
#     param1, param2 = param2, param1

#     print("After swapping:")
#     print("Parameter 1 is", param1)
#     print("Parameter 2 is", param2)

# swap(15, 20)

# Write a Python program to create a dictionary with keys as student names and values as their
# corresponding grades. Then, perform the following operations:
# i. Add a new student and grade to the dictionary.
# ii. Update the grade of an existing student.
# iii. Remove a student from the dictionary.
# iv. Print all student names and their grades.

#create an empty Dictonary to sstore student name & grade
student={}
#add grades using dictionary
def add_students(name, grade):
    student[name]=grade
    print(f"Added Student'{name}' with grade '{grade}'.")

#funvtions to updaete the grade of an existing student
def update_grade(name, new_grade):
    if name is student:  # it is searchinf for the key name
        student[name] = new_grade
        print(f"Added studen '{name}'to '{new_grade}'")
    else:
        print(f"Student'{name}' not found.")

# #function to print all students names and their grades
# def print_students():
#     print("Student Name\t Grade") #\t mean  tab it add 4 spaces after word
#     for name, grade in students.items():
        