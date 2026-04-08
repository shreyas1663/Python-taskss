from functionss import *

while True:
    print("\n****************** SMART EXPENSE MANAGER ******************")
    print("1. Add User")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Filter by Category")
    print("5. Filter by Date")
    print("6. Total Expense")
    print("7. Category Wise Report")
    print("8. Monthly Report")
    print("9. Highest Expense")
    print("10. Smart Insight")
    print("11. Update Expense")
    print("12. Deleting Expense")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        user = User(name)
        user.add()

    elif choice == 2:
        user_id = int(input("User ID: "))
        amount = float(input("Amount: "))
        category = input("Category: ")
        desc = input("Description: ")
        date = input("Date (YYYY-MM-DD): ")

        exp = Expense(user_id, amount, category, desc, date)
        exp.add()

    elif choice == 3:
        uid = int(input("User ID: "))
        data = view_expenses(uid)

    elif choice == 4:
        uid = int(input("User ID: "))
        data = view_expenses(uid)
        cat = input("Enter category: ")
        print(filter_by_category(data, cat))

    elif choice == 5:
        uid = int(input("User ID: "))
        data = view_expenses(uid)
        date = input("Enter date (YYYY-MM-DD): ")
        print(filter_by_date(data, date))

    elif choice == 6:
        uid = int(input("User ID: "))
        data = view_expenses(uid)
        print("Total:", total_expense(data))

    elif choice == 7:
        uid = int(input("User ID: "))
        data = view_expenses(uid)
        print(category_wise(data))

    elif choice == 8:
        uid = int(input("User ID: "))
        print(monthly_report(uid))

    elif choice == 9:
        uid = int(input("User ID: "))
        data = view_expenses(uid)
        print("Highest:", highest_expense(data))

    elif choice == 10:
        uid = int(input("User ID: "))
        data = view_expenses(uid)
        smart_insight(data)

    elif choice == 11:
        exp_id = int(input("Expense ID: "))
        amount = float(input("New Amount: "))
        update_expense(exp_id, amount)

    elif choice == 12:
        exp_id = int(input("Enter Expense ID to delete: "))
        delete_expense(exp_id)

    elif choice == 0:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")

