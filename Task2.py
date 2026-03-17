print("----- Bitwise Operator Tasks -----")

# a&b
a = 10
b = 6
print("a&b = ", a & b)

# a|b
x = 12
y = 5
print("a|b = ", x | y)

# ~num
num = 8
print("~num = ", ~num)

# a^b
a = 15
b = 9
print("a^b = ", a ^ b)

# Left Shift
num = 7
print("Left Shift = ", num << 2)

# Right Shift
num = 20
print("Right Shift = ", num >> 1)

# input and output for AND
a = int(input("Enter first number for AND: "))
b = int(input("Enter second number for AND: "))
print("AND:", a & b)

# input and output for XOR
a = int(input("Enter first number for XOR: "))
b = int(input("Enter second number for XOR: "))
print("XOR:", a ^ b)


print("\n----- String Tasks -----")

# Replication
s = "hi"
print( s * 4)

# Repetition
s = "python"
print("Repetition:", s * 3)

# Concatenation
a = "super"
b = "man"
print("Concatenation:", a + b)

# Concatenation with space
a = "hello"
b = " "
c = "world"
print("Concatenation with space:", a + b + c)

# user input and replication
name = input("Enter name: ")
print("User input and replication:", name * 5)

# input and concatenation
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Input and concatenation:", s1 + s2)


print("\n----- Input & Type Casting Tasks -----")

# input and type
name = input("Enter name: ")
print("input and type:", type(name))

# input and type casting
age = int(input("Enter age: "))
print("input and type casting:", age)

# input and addition
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
print("input and addition:", a + b)

# input and average
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
avg = (m1 + m2) / 2
print("input and average:", avg)

# input and expression
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("input and expression:", 3*a*2 + b - 2)

# input and type conversion
num = input("Enter number: ")
print("before:", type(num))
num = int(num)
print("after:", type(num))


print("\n----- Unit Digit Tasks -----")

# 21
num = input("Enter number: ")
print("21:", num[-1])

# 22
num = int(input("Enter number: "))
print("22:", num % 10)

# 23
num = int(input("Enter number: "))
print("23:", num // 10)

# 24
num = int(input("Enter number: "))
print("24:", (num // 10) % 10)

# 25
num = int(input("Enter 5 digit number: "))
print("25:", num % 10)


print("\n----- If Statement Tasks -----")

# 26
if 10 >= 5:
    print("26: Condition True")

# 27
num = int(input("Enter number: "))
if num > 50:
    print("27: Greater than 50")

# 28
age = int(input("Enter age: "))
if age >= 18:
    print("28: Eligible")

# 29
num = int(input("Enter number: "))
if num > 100:
    print("29: Greater than 100")

# 30
num = int(input("Enter number: "))
if num >= 0:
    print("30: Non-negative number")


print("\n----- If Else Tasks -----")

# 31
num = int(input("Enter number: "))
if num % 2 == 0:
    print("31: Even")
else:
    print("31: Odd")

# 32
marks = int(input("Enter marks: "))
if marks >= 35:
    print("32: Pass")
else:
    print("32: Fail")

# 33
num = int(input("Enter number: "))
if num > 0:
    print("33: Positive")
else:
    print("33: Negative")

# 34
num = int(input("Enter number: "))
if num > 10:
    print("34: Greater than 10")
else:
    print("34: Not greater than 10")


print("\n----- Nested If Tasks -----")

# 35
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("35: Selected")
        else:
            print("35: Rejected")
    else:
        print("35: Rejected")
else:
    print("35: Rejected")

# 36
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("36: Admission Granted")
    else:
        print("36: Age not eligible")
else:
    print("36: Marks not eligible")

# 37
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("37: Selected")
        else:
            print("37: Rejected")
    else:
        print("37: Rejected")
else:
    print("37: Rejected")


print("\n----- Match Statement Tasks -----")

# 38
day = int(input("Enter number (1-7): "))
match day:
    case 1:
        print("38: Sunday")
    case 2:
        print("38: Monday")
    case 3:
        print("38: Tuesday")
    case 4:
        print("38: Wednesday")
    case 5:
        print("38: Thursday")
    case 6:
        print("38: Friday")
    case 7:
        print("38: Saturday")

# 39
num = int(input("Enter number (1-3): "))
match num:
    case 1:
        print("39: Red")
    case 2:
        print("39: Blue")
    case 3:
        print("39: Green")

# 40
num = int(input("Enter number (1-4): "))
match num:
    case 1:
        print("40: Apple")
    case 2:
        print("40: Mango")
    case 3:
        print("40: Orange")
    case 4:
        print("40: Banana")