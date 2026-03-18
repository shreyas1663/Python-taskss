#LOOP BASICS
#for loop
#01
for i in range (1, 11) :
    print(i)

#02
for i in range (1,101):
    if i%2 == 0:
        print(i)

#03
for i in range (1,101):
    if i%2 == 1:
        print(i)

#04
for i in range (1,11) :
    multiplication = i * 7
    print("7 * ",i,"=",multiplication)

#05
sum = 0
for i in range (1,101):
   sum += i
print(sum)

#06
for i in range (1,51):
    sub = 51 - i
    print(sub)

#07
count = 0
for i in range (1,101):
    if i%3 == 0:
        count += 1
print(count)

#08
for i in range (1,11):
    print(i**2)

#09
for i in range (1,11):
    print(i**3)

#10
num=input(int())
for i in range (1,int(num)):
    print(i)

#While loop

#11
num = 1
while num <= 20:
    print(num)
    num += 1

#12
n = int(input())
fa = 1
i = 1
while i<=n:
    fa *=i
    i += 1
print(fa)

#13
num = int(input())
reversed_num = 0
while num != 0:
    rev = num % 10
    reversed_num = reversed_num * 10 + rev
    num = num // 10 
print(reversed_num)

#14
num = int(input())
count = 0
if num == 0:
   print(1)
else:
    while num > 0:
        count1 = num % 10
        count +=1
        num = num//10
    print(count)

#15
while True:
    n= input("Let's talk ")
    if n == "stop":
        break


#nested loops

#Print Pattren
n = int(input())
for i in range(1,n):
    print("* " * i)

#print pattern

n = int(input())
for i in range (1,n):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Multiplication of 1 to 5 uaing nested loop

for i in range (1,6):
    for j in range (1,11):
        print(i," * ",j," = ",i*j)

#Printing statement
n = input()
for i in range (1,4):
    print(n)


#Pint
n = 1
for i in range (3):
    for j in range (3):
        print(n,end=" ")
        n +=1
    print()


#String Basics
#21
n = input()
count = 0
for i in n:
    count += 1
print(count)

#22

n = input()
vowels = "aeiouAEIOU"
count = 0
for i in n:
    if i in vowels:
        count += 1
print(count)

#23
n = input()
vowels = "aeiouAEIOU"
count = 0
for i in n:
    if i not in vowels:
        count += 1
print(count)

#24
n = input()
rev = ""
for i in n:
    rev = i + rev
print(rev)

#25
n = input()
rev = ""
for i in n:
    rev = i + rev
if i == rev:
    print("Palindrome")
else:
    print("not palindrome")

#string slicing

#26
s = input("enter string = ")
print(s[:5])

#27
s = input("enter string = ")
print(s[-3:])

#28
s = input("enter string = ")
print(s[::-1])

#29
s = input("enter string = ")
print(s[::2])

#30
s = input("enter string = ")
print(s[1:-1])

#List Basics
#31
num = [10,20,30,40,50]
total = 0
for i in num:
    total += i
print(total)


#32
nums = [10,20,30,40,50]
maxi = nums[0]
for i in nums:
    if i > maxi:
        maxi = i
print(maxi)

#33
nums = [10,20,30,40,50]
mimm = nums[0]
for i in nums:
    if i < mimm:
        mimm = i
print(mimm)

#34
nums = [10,20,30,40,50]

count = 0
for n in nums:
    count += 1
print(count)

#35

nums = [10,20,30,40,50]
v = int(input())
if v in nums:
    print("Exist")
else:
    print("not Exist")

#36

nums = [10,20]
nums.append(30)
nums.append(30)
nums.append(30)
print(nums)

#37

nums =[10,20,30,40]
nums.insert(2,25)
print(nums)

#38
nums =[10,20,30,40]
nums.remove(30)
print(nums)

#39
nums =[10,20,30,40]
rev = []
for i in range (len(nums)-1,-1,-1):
    rev.append(nums[i])
print(rev)

#40
nums =[10,20,30,40]
n = len(nums)
for i in range(n):
    for j in range(0, n-i-1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)