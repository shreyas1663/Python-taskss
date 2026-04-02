# class User:
#     def __init__(self,name,id_num):
#         self.name   = name
#         self.id_num = id_num
#
#
# class Student(User):
#     def __init__(self,name,id_num,dept,fees):
#         super().__init__(name,id_num)
#         self.dept = dept
#         self.fees = fees
#
# class Faculty(User):
#     def __init__(self,name,id_num,salary):
#         super().__init__(name,id_num)
#         self.salary = salary
#
# class TempFaculty(Faculty):
#     def __init__(self,name,id_num,salary,duration):
#         super().__init__(name,id_num,salary)
#         self.duration = duration

########## application of Abstraction ###########
# from abc import ABC, abstractmethod
# class AbstractUser(ABC):
#     @abstractmethod
#     def get_details(self):
#         pass
#
# class User(AbstractUser):
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def get_details(self):
#         return f"Name: {self.name}, ID: {self.id}"
#
#
# class Student(User):
#     def __init__(self, name, id, dept, fees):
#         super().__init__(name, id)
#         self.dept = dept
#         self.fees = fees
#
#     def get_details(self):
#         return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"
#
# class Faculty(User):
#     def __init__(self, name, id, salary):
#         super().__init__(name, id)
#         self.salary = salary
#
#     def get_details(self):
#         return f"{super().get_details()}, Salary: {self.salary}"
#
# class TempFaculty(Faculty):
#     def __init__(self, name, id, salary, duration):
#         super().__init__(name, id, salary)
#         self.duration = duration
#
#     def get_details(self):
#         return f"{super().get_details()}, Duration: {self.duration}"
#
#
################## using the Lambda function ###############################
# class Student:
#     def __init__(self, name, id, dept, fees):
#         self.name = name
#         self.id = id
#         self.dept = dept
#         self.fees = fees
#
#     def __repr__(self):
#         return f"{self.name} - Fees: {self.fees}"
#
# class Faculty:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary
#
#     def __repr__(self):
#         return f"{self.name} - Salary: {self.salary}"
#
# students = [
#     Student("Shreyas", 101, "CSE", 50000),
#     Student("Amit", 102, "ECE", 30000),
#     Student("Ravi", 103, "ME", 40000)
# ]
# students.sort(key=lambda x: x.fees)
#
# print("Students sorted by fees:")
# for s in students:
#     print(s)
#
# faculty_list = [
#     Faculty("Anil", 201, 60000),
#     Faculty("Kiran", 202, 45000),
#     Faculty("Suresh", 203, 70000)
# ]
# faculty_list.sort(key=lambda x: x.salary)
#
# print("\nFaculty sorted by salary:")
# for f in faculty_list:
#     print(f)

########################### Using the map() ##################################
# class Student:
#     def __init__(self, name, id, dept, fees):
#         self.name = name
#         self.id = id
#         self.dept = dept
#         self.fees = fees
#
# students = [
#     Student("Shreyas", 101, "CSE", 50000),
#     Student("Amit", 102, "ECE", 30000),
#     Student("Ravi", 103, "ME", 40000)
# ]
# names = list(map(lambda s: s.name, students))
#
# print(names)

########################## using the filter() #############################
# class Student:
#     def __init__(self, name, id, dept, fees):
#         self.name = name
#         self.id = id
#         self.dept = dept
#         self.fees = fees
#
#     def __repr__(self):
#         return f"{self.name} - Fees: {self.fees}"
# class Faculty:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary
#
#     def __repr__(self):
#         return f"{self.name} - Salary: {self.salary}"
# students = [
#     Student("Shreyas", 101, "CSE", 50000),
#     Student("Amit", 102, "ECE", 30000),
#     Student("Ravi", 103, "ME", 60000)
# ]
# faculty_list = [
#     Faculty("Anil", 201, 60000),
#     Faculty("Kiran", 202, 25000),
#     Faculty("Suresh", 203, 35000)
# ]
# high_fee_students = list(filter(lambda s: s.fees > 50000, students))
# high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))
# print("Students with fees > 50000:")
# for s in high_fee_students:
#     print(s)
#
# print("\nFaculty with salary > 30000:")
# for f in high_salary_faculty:
#     print(f)


############################## Using reduce() ################################
# class Student:
#     def __init__(self, name, id, dept, fees):
#         self.name = name
#         self.id = id
#         self.dept = dept
#         self.fees = fees
# class Faculty:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary


############################# Using Higer order function ###########################
# class Student:
#     def __init__(self, name, id, dept, fees):
#         self.name = name
#         self.id = id
#         self.dept = dept
#         self.fees = fees
#
#     def __repr__(self):
#         return f"{self.name} - Fees: {self.fees}"
#
# def process_users(users, func):
#     return list(map(func, users))

############################### mini system #############################

from abc import ABC, abstractmethod
from functools import reduce

class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"{super().get_details()}, Dept: {self.dept}, Fees: {self.fees}"

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"{super().get_details()}, Salary: {self.salary}"

def process_users(users, func, condition=None):
    if condition:
        users = filter(condition, users)
    return list(map(func, users))



