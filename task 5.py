########## Task 1 :- user info manager ###########

user = []

def create_user(name,age,role):
    data = {"name": name,"age": age,"role":role}
    user.append(data)
    return data

name = input("enter your name:- ")
age = int(input("enter your age:- "))
role = input("enter the role:- ")

create_user(name,age,role)
print(f"{user[-1]['name'].title()} is {user[-1]['age']} years old and works as a {user[-1]['role']}")


########## Task 2 :- dynamic calculator ###########

def calculate_total(*numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

numbers = []
n = int(input("how many numbers do you want to enter?\n" ))
for i in range(n):
    num = float(input("enter the numbers: "))
    numbers.append(num)
total, average = calculate_total(*numbers)
print(f"Total: {total}, Average: {average}")

########## Task 3 :- keyword config system ###########

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")
system_config(mode="debug", version="1.0")

########## Task 4 :- factorial service ###########

def fact(n):
    if n < 0:
        print("negative numbers are not allowed") 
        return None
    
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n - 1)

number = int(input("enter the number "))

result = fact(number)
print(f"The factorial of {number} is {result}")


########### Task 5 :-  Memory Optimization ###########

def square_generator(n):
    for i in range(n):
        yield i * i

def square_list(n):
    return [i * i for i in range(n)]

n = int(input("enter the number of squares to generate: "))
gen = square_generator(5)
lst = square_list(5)

print(gen,type(gen))
print(lst,type(lst))

###### Task 6 :-   Exception Handling Module ###########


def divide():
    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))
        
        result = numerator / denominator
        print("Result:", result)
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    except ValueError:
        print("Error: Invalid input (please enter numbers only)")
    
    finally:
        print("Program Completed")

divide()

####### Task 7 :-  File Handling System ###########

file = open("example.txt", "w")
file.write("Hello, this is a sample file.\n")
file.write("This file is used for demonstrating file handling in Python.\n")
file.close()

