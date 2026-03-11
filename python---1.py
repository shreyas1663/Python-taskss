#------Printing Formate------

print("--------Printing Formate--------\n")
print("Hello World",end=" ")
print("Welcome to Python")
print("Laptop","Mouse","Keyboard",sep=" | ",end="\n\n")

#------Variables------

print("--------Variables--------\n")
name = "Ravi"
age = 22
city = "Chennai"
print(name,age,city,sep="-",end="\n\n")

#------Multiple Assignment------

print("--------Multiple Assignment--------\n")
name,age,student = "Meena",20,True
print(name,age,student,"\n")

#------Indexing------

print("--------Indexing--------\n")
word = "Python"
print(word[0],word[2],word[5],sep="\n",end="\n\n")

#------Arithmetic Operators------

print("--------Arithmetic Operators--------\n")
print(25+10) #Addition
print(50-20) #Subtraction
print(8*5) #Multiplication
print(100/10) #Division
print(20//3) #Floor Division
print(10%3) #Modulus
print(2**4,"\n") #Exponentiation

#------BODMAS Expression------
print("--------BODMAS Expression--------\n")
print(3+2*5**2,end="\n") #BODMAS: Brackets, Orders (i.e. powers and square roots, etc.), Division and Multiplication, Addition and Subtraction

#------Assignment Operators------
print("--------Assignment Operators--------\n")
num = 50
num += 25
print(num)
num1 = 100
num1 /=10
print(num1,"\n")

#------Comparison Operators------
print("--------Comparison Operators--------\n")
print(10 > 5) #Greater than
print(20 < 15) #Less than
print(5 == 5) #equal to
print(10 != 8) #Not equal to
print(7 >= 7) #Greater than or equal to
print(6 <= 2,end="\n\n") #Less than or equal to

#------String Comparison------
print("--------String Comparison--------\n")
a = "apple"
b = "Apple"
print(a == b,end="\n\n") #False, because of case sensitivity

#------Logical Operators------
print("--------Logical Operators--------\n")
print(10  > 5 and 5 == 5)#True, because both conditions are true
print(5  > 10 or 10 == 10)#True, because one of the conditions is true
print(not(5 > 2),end="\n\n")#True, because 5 is not greater than 10

#------Membership Operators------
print("--------Membership Operators--------\n")
numbers = [10,20,30,40,50]
print(20 in numbers) #True, because 20 is in the list
print(60 in numbers) #False, because 60 is not in the list
print(30 not in numbers,end="\n\n") #True, because 30 is not in the list

#------Swapping Variables------
print("--------Swapping Variables--------\n")
a = 10
b = 20
a,b = b,a
print("a =",a)
print("b =",b,end="\n\n")

#------Bitwise Operators------
print("--------Bitwise Operators--------\n")
a = 6
b = 3
print(a ^ b)
