class UserEncap:
    def _init_(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user: {self.__user_name}")

    def login(self):
        print(f"Logging in: {self.__user_name}")


# Run Encapsulation
print("User Registration and Login - Encapsulation Demo")

u1 = UserEncap()
u1.set_user("john", "1234")
u1.register()
u1.login()


# =========================================
# Inheritance Example
# =========================================

class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged In")


class Student(User):
    def student_greet(self):
        print("Hello Student")


class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Run Inheritance
print("\nRole-Based Access System - Inheritance Demo")

s = Student()
s.register()
s.login()
s.student_greet()

f = Faculty()
f.register()
f.faculty_greet()

t = TempFaculty()
t.register()
t.faculty_greet()
t.tempFaculty_greet()


# =========================================
# Method Overriding Example
# =========================================

class UserOverride:
    def greet(self):
        print("Welcome User")


class StudentOverride(UserOverride):
    def greet(self):
        print("Welcome Student")


class FacultyOverride(UserOverride):
    def greet(self):
        print("Welcome Faculty")


# Run Method Overriding
print("\nCustomized Greetings - Method Overriding Demo")

s2 = StudentOverride()
f2 = FacultyOverride()

s2.greet()
f2.greet()


# =========================================
# Method Chaining Example
# =========================================

class UserChain:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self


# Run Method Chaining
print("\nUser Actions Flow - Method Chaining Demo")

uc = UserChain()
uc.login().greet().register()


# =========================================
# Real-Time Mini User System
# =========================================

class UserSystem:
    users_count = 0

    def _init_(self, username, pwd):
        self.__username = username
        self.__pwd = pwd
        UserSystem.users_count += 1

    def login(self):
        print(f"{self.__username} logged in")
        return self

    def register(self):
        print(f"{self.__username} registered")
        return self

    def greet(self):
        print("Welcome User")
        return self


class StudentSystem(UserSystem):
    def greet(self):
        print("Welcome Student")
        return self


class FacultySystem(UserSystem):
    def greet(self):
        print("Welcome Faculty")
        return self


# Run Combined System
print("\nMini User Management System")

stu = StudentSystem("karthik", "123")
fac = FacultySystem("admin", "456")

stu.login().greet().register()
fac.login().greet().register()

print("Total users:", UserSystem.users_count)