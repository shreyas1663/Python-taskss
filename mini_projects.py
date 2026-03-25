
######### mini project 1:- Employee Management System #########

employee = []

def add_emp(y):
    name = input("Enter the employee name:-")
    age = int(input("Enter the age of the employee:-"))
    role = input("Enter the role of the employee:-")
    salary = float(input("Enter the salary of the employee:-"))

    emp = {"name": name,"age": age,"role": role,"salary": salary}
    employee.append(emp)

def update_emp():
    name = input ("enter the name of the employee that you want to update:-")
    for empp in employee:
        if empp["name"] == name:
            name1 = input("Enter the new name of the employee:-")
            age = int(input("Enter the ageof the employee:-"))
            role = input("Enter the role")
            salary = float(input("Enter the salary of the employee:-"))
            empp["name"] = name1
            empp["age"] = age 
            empp["role"] = role
            empp["salary"] = salary

def delete_emp():
    name =input("Enter the employeename that you want to delete:- ")
    for empp in employee:
        if empp["name"] == name:
            employee.remove(empp)

def display_perticular_emp():
    name = input("Enter the name of the employee you want to display:- ")
    for empp in employee:
        if empp["name"] == name:
            print("Name:-", empp["name"])
            print("Age:-", empp["age"])
            print("Role:-", empp["role"])
            print("Salary:-", empp["salary"])

def display_all_emp():
    for emmp in employee:
        print("Name:-", emmp["name"])
        print("Age:-", emmp["age"])
        print("Role:-", emmp["role"])
        print("Salary:-", emmp["salary"])


while True:
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Display Particular Employee")
    print("5. Display All Employees")
    print("6. Exit")

    choice = int(input("Enter your choice:- "))
    if choice == 1:
        add_emp(employee)
    elif choice == 2:
        update_emp()
    elif choice == 3:
        delete_emp()
    elif choice == 4:
        display_perticular_emp()
    elif choice == 5:
        display_all_emp()
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")



# ########## mini project 2:- Student Management System #########

students = []

def add_std():
    name = input("Enter the student name:- ")
    eng = float(input("Enter the English marks:- "))
    kannada = float(input("Entaer the Kannada Marks:- "))
    hindi = float(input("Enter the Hindi Marks:- "))

    std = {"name": name, "English": eng, "Kannada": kannada, "Hindi": hindi}
    students.append(std)

def total_average():
    for name in students:
        if name["name"] == input("Enter the name of the student:-"): 
            total = name["English"] + name["Kannada"] + name["Hindi"]
            average = total / 3
            print(f" The average of {name['name']}: {average}")

            if average >=80 and average <=100:
                print(f"The grade of {name['name']} is:- A")
            elif average >=70 and average <80:
                print(f"The grade of {name['name']} is:- B")
            elif average >=60 and average <70:
                print(f"The grade of {name['name']} is:- C")
            elif average >=40 and average <60:
                print(f"The grade of {name['name']} is:- D") 
            else:
                print(f"The grade of {name['name']} is:- F")
        else:
            print("Student not found.")           
while True:
    print("1.Add student details")
    print("2.Calculate average marks and grade")
    print("3.Exit")
    choice = int(input("Enter the choice:- "))
    if choice == 1:
        add_std()
    elif choice == 2:
        total_average()
    elif choice == 3:
        break
    else:
        print("Invalid choice.plese try again.")


 ######### mini project 3:- Shopping Cart Management System #########

items = []

def add_item():
    name = input("enter the item name:- ")
    price = float(input("enter the price of the item :-"))

    total_item = {"name": name, "price": price}
    items.append(total_item)

def total_bill():
    total = 0
    for item in items:
        total += item["price"]
        print(f"total bill is :- {total}")

def remove_item():
    name = input("Enter the name of the item you want to remove:- ")
    for item in items:
        if item["name"] == name:
            items.remove(item)
            print(f"your item {name} has been removed from the cart.")

def display_cart():
    if not items:
        print("You not yet added any items to the cart.")
    else:
        print("Items in your cart:-")
        for item in items:
            print(f"Name:- {item['name']}, Price:- {item['price']}")

while True:
    print("1. Add item to cart")
    print("2. Remove item from cart")
    print("3. Display items in cart")
    print("4. Calculate total bill")
    print("5. Exit")

    choice = int(input("Enter the your choice:- "))

    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        display_cart()
    elif choice == 4:
        total_bill()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")


########## mini project 4:- login and user validation Management System #########
user = []
def registration():
    name = input("enter the username:- ")
    password = input("enter the password:- ")
    reg = {"username": name, "password": password}
    user.append(reg)

def login():
    name = input("Enter the useranme:- ")
    password = input("Enter the Password:- ")
    for user2 in user:
        if user2["username"] == name and user2["password"] == password:
            print("Login successfull......:)")
            return
    print("Login failed......:( Invalid username or password.")

while True:
    print("1. Registration")
    print("2. Login")
    print("3. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        registration()
    elif choice == 2:
        login()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")



########### mini project 5:-  uniqe Visitor Counter #########

s = set()
def add_visitor():
    name = input("Enter the name of the visitor:- ")
    s.add(name)
    print(f"Visitor {name} added to the counter.")

def display_count():
    count = len(s)
    print(f"Total unique visitors: {count}")

while True:
    print("1. Add Visitor")
    print("2. Display Unique Visitor Count")
    print("3. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        add_visitor()
    elif choice == 2:
        display_count()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")


########### mini project 6:-  String formatter tool #########

name= input("Enter your name:- ")
product = input("Enter Product name:- ")
message = f"Hello {name}, thank you for purchasing {product} from our store!"
print("\n String Formatter Tool")
print("Left Aligned:-{message:<50}".format(message=message))
print("Right Aligned:-{message:>50}".format(message=message))
print("Center Aligned:-{message:^50}".format(message=message))

########## mini project 7:-  Bank Account System  #########
acc = []
def create_account():
    name = input("Enter your Name :- ")
    balance = float(input("Enter the initial balance:- "))
    account = {"name": name, "balance": balance}
    acc.append(account)
    print(f"Account created for {name} with initial balance ${balance:.2f}")

def deposit():
    name = input("Enter your Name :- ")
    amount = float(input("Enter the amount you want to deposit:-  "))
    for account in acc:
        if account["name"] == name:
            account["balance"] += amount
            print(f"Deposited ${amount:.2f} to {name}'s account. New balance: ${account['balance']:.2f}")
            
def withdraw():
    name = input("Enter the name :- ")
    amount = float(input("Enter the amount you want to withdraw:- "))
    for account in acc:
        if account["name"] == name:
            if account["balance"]>= amount:
                account["balance"] -= amount
                print(f"Withdrew ${amount:.2f} from {name}'s account. New balance: ${account['balance']:.2f}")
            else:
                print("Insufficient balance.")  
def check_balance():
    name = input("Enter the name:- ")
    for account in acc:
        if account["name"] == name:
            print(f"{name}'s account balance: ${account['balance']:.2f}")
while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

############# mini project 8:- Voting System  #########

voters = []
def register_voter():
    candidate = input("Enter your name:- ")
    vote = input("Enter the candidate you want to vote for:- ")
    voter = {"name": candidate, "vote": vote}
    voters.append(voter)
def display_results():
    results = {}
    for voter in voters:
        candidate = voter["vote"]
        if candidate in results:
            results[candidate] += 1
        else:
            results[candidate] = 1
    print("Voting Results:")
    for candidate, votes in results.items():
        print(f"{candidate}: {votes} votes")
while True:
    print("1. Register Voter")
    print("2. Display Voting Results")
    print("3. Exit")
    choice = int(input("Enter your choice:- "))
    if choice == 1:
        register_voter()
    elif choice == 2:
        display_results()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")


############# mini project 9:-  Course Enrollment System  #########

# Course Enrollment System

students = []
def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")

    courses = [course.strip() for course in courses]

    student = {
        "name": name,
        "courses": courses
    }

    students.append(student)
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No students found!\n")
        return

    print("\nStudent Details:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}")
        print(f"   Courses: {', '.join(student['courses'])}")
    print()


# ➤ Update Courses
def update_courses():
    display_students()
    index = int(input("Enter student number to update courses: ")) - 1

    if 0 <= index < len(students):
        print("1. Add Course")
        print("2. Remove Course")
        choice = input("Enter choice: ")

        if choice == '1':
            new_course = input("Enter course to add: ")
            students[index]['courses'].append(new_course)
            print("Course added!\n")

        elif choice == '2':
            remove_course = input("Enter course to remove: ")
            if remove_course in students[index]['courses']:
                students[index]['courses'].remove(remove_course)
                print("Course removed!\n")
            else:
                print("Course not found!\n")

        else:
            print("Invalid choice!\n")
    else:
        print("Invalid student number!\n")

def menu():
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Courses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_courses()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

########### task 10:- Number Utility Tool  #########

def convert_number(num):
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")
    print()


def format_number(num):
    print(f"Formatted Number: {num:,}")
    print()

def scientific_notation(num):
    print(f"Scientific Notation: {num:.2e}")
    print()


def menu():
    while True:
        print("1. Convert Number (Binary/Octal/Hex)")
        print("2. Format Number (Comma Separator)")
        print("3. Scientific Notation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            num = int(input("Enter an integer: "))
            convert_number(num)

        elif choice == '2':
            num = float(input("Enter a number: "))
            format_number(num)

        elif choice == '3':
            num = float(input("Enter a number: "))
            scientific_notation(num)

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.\n")
