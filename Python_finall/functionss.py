import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod
from datetime import datetime

# DB Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="expense_db"
)

cursor = conn.cursor()


# Abstract Base Class
class BaseManager(ABC):
    @abstractmethod
    def add(self):
        pass


# User Class
class User(BaseManager):

    def __init__(self, name):
        self.__name = name

    def add(self):
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (self.__name,))
        conn.commit()
        print("User Added Successfully")


# Expense Class
class Expense(User):

    def __init__(self, user_id, amount, category, desc, date):
        self.__user_id = user_id
        self.__amount = amount
        self.__category = category
        self.__desc = desc
        self.__date = date

    def add(self):
        query = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (self.__user_id, self.__amount,
                               self.__category, self.__desc, self.__date))
        conn.commit()
        print("Expense Added")


# View Expenses
def view_expenses(user_id):
    query = """
    SELECT users.name, expenses.amount, expenses.category,
           expenses.description, expenses.date
    FROM expenses
    JOIN users ON users.user_id = expenses.user_id
    WHERE users.user_id = %s
    """
    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    for row in data:
        print(row)

    return data


# Filters
def filter_by_category(data, category):
    return list(filter(lambda x: x[2] == category, data))


def filter_by_date(data, date):
    return [i for i in data if str(i[4]) == date]


# Total Expense
def total_expense(data):
    amounts = list(map(lambda x: x[1], data))
    return reduce(lambda a, b: a + b, amounts, 0)


# Category Wise
def category_wise(data):
    categories = set([i[2] for i in data])

    return {cat: sum([i[1] for i in data if i[2] == cat])
            for cat in categories}


# Update
def update_expense(exp_id, amount):
    query = "UPDATE expenses SET amount=%s WHERE exp_id=%s"
    cursor.execute(query, (amount, exp_id))
    conn.commit()
    print("Updated")


# Monthly Report
def monthly_report(user_id):
    query = """
    SELECT MONTH(date), SUM(amount)
    FROM expenses
    WHERE user_id = %s
    GROUP BY MONTH(date)
    """
    cursor.execute(query, (user_id,))
    return cursor.fetchall()


# Highest Expense
def highest_expense(data):
    return reduce(lambda a, b: a if a[1] > b[1] else b, data)


# Smart Insight
def smart_insight(data):
    cat_data = category_wise(data)
    highest = max(cat_data, key=cat_data.get)
    print(f"You are spending too much on {highest}")

def delete_expense(exp_id):
    query = "DELETE FROM expenses WHERE exp_id = %s"
    cursor.execute(query, (exp_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Expense Deleted Successfully")
    else:
        print("Expense ID not found")
