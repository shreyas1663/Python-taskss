# from parent import Student,Faculty,TempFaculty
# s1 = Student("Shreyas", 101, "CSE", 50000)
# f1 = Faculty("Ravi", 201, 60000)
# t1 = TempFaculty("Anil", 301, 40000, "6 months")
#
# print(s1.name, s1.id_num, s1.dept, s1.fees)
# print(f1.name, f1.id_num, f1.salary)
# print(t1.name, t1.id_num, t1.salary, t1.duration)


# s1 = Student("Shashank", 102, "ISE", 50000)
# f1 = Faculty("Ravi kumar", 202, 60000)
# t1 = TempFaculty("Abhi", 301, 40000, "6 months")
# print(s1.get_details())
# print(f1.get_details())
# print(t1.get_details())



# from parent import Student,Faculty,reduce
#
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
# total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
# total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)
# print("Total Fees:", total_fees)
# print("Total Salary:", total_salary)

# from parent import Student,process_users
# students = [
#     Student("Shreyas", 101, "CSE", 50000),
#     Student("Amit", 102, "ECE", 30000),
#     Student("Ravi", 103, "ME", 60000)
# ]
# names = process_users(students, lambda s: s.name)
# fees = process_users(students, lambda s: s.fees)
# print("Names:", names)
# print("Fees:", fees)

from parent import Student,process_users,Faculty,reduce
students = [
    Student("Shreyas", 101, "CSE", 50000),
    Student("Amit", 102, "ECE", 30000),
    Student("Ravi", 103, "ME", 60000)
]

faculty_list = [
    Faculty("Anil", 201, 60000),
    Faculty("Kiran", 202, 25000),
    Faculty("Suresh", 203, 35000)
]

print("ALL STUDENTS:")
for s in students:
    print(s.get_details())

print("\n ALL FACULTY:")
for f in faculty_list:
    print(f.get_details())

students.sort(key=lambda s: s.fees)
faculty_list.sort(key=lambda f: f.salary)

print("\n SORTED STUDENTS (by fees):")
for s in students:
    print(s.get_details())

print("\n SORTED FACULTY (by salary):")
for f in faculty_list:
    print(f.get_details())

high_fee_students = list(filter(lambda s: s.fees > 40000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty_list))

print("\n HIGH FEE STUDENTS:")
for s in high_fee_students:
    print(s.get_details())

print("\n HIGH SALARY FACULTY:")
for f in high_salary_faculty:
    print(f.get_details())

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty_list, 0)

print("\n TOTAL FEES:", total_fees)
print("TOTAL SALARY:", total_salary)

print("\n STUDENT NAMES (map using HOF):")
names = process_users(students, lambda s: s.name)
print(names)
print("\n HIGH FEE STUDENT NAMES (map + filter using HOF):")
high_names = process_users(
    students,
    lambda s: s.name,
    lambda s: s.fees > 40000
)
print(high_names)
