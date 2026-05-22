import sqlite3
from datetime import datetime

conn = sqlite3.connect("bank1.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    balance REAL,
    created_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_no INTEGER,
    type TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()

# ================= FUNCTIONS =================

def create_account():
    try:
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        if balance < 0:
            print("Balance cannot be negative")
            return

        created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            "INSERT INTO accounts (name, balance, created_date) VALUES (?, ?, ?)",
            (name, balance, created_date)
        )
        conn.commit()

        acc_no = cursor.lastrowid
        print("Account Created Successfully")
        print("Your Account Number is:", acc_no)

    except ValueError:
        print("Invalid input")


def deposit():
    try:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero")
            return

        cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (acc_no,))
        result = cursor.fetchone()

        if not result:
            print("Account not found")
            return

        new_balance = result[0] + amount
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            "UPDATE accounts SET balance=? WHERE account_no=?",
            (new_balance, acc_no)
        )

        cursor.execute(
            "INSERT INTO transactions (account_no, type, amount, date) VALUES (?, ?, ?, ?)",
            (acc_no, "Deposit", amount, date)
        )

        conn.commit()
        print("Deposit Successful")

    except ValueError:
        print("Invalid input")


def withdraw():
    try:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero")
            return

        cursor.execute("SELECT balance FROM accounts WHERE account_no=?", (acc_no,))
        result = cursor.fetchone()

        if not result:
            print("Account not found")
            return

        if result[0] < amount:
            print("Insufficient Balance")
            return

        new_balance = result[0] - amount
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            "UPDATE accounts SET balance=? WHERE account_no=?",
            (new_balance, acc_no)
        )

        cursor.execute(
            "INSERT INTO transactions (account_no, type, amount, date) VALUES (?, ?, ?, ?)",
            (acc_no, "Withdraw", amount, date)
        )

        conn.commit()
        print("Withdrawal Successful")

    except ValueError:
        print("Invalid input")


def show_account():
    try:
        acc_no = int(input("Enter Account Number: "))
        cursor.execute("SELECT * FROM accounts WHERE account_no=?", (acc_no,))
        result = cursor.fetchone()

        if not result:
            print("Account not found")
            return

        print("\n--- Account Details ---")
        print("Account No:", result[0])
        print("Name:", result[1])
        print("Balance:", result[2])
        print("Created Date:", result[3])

    except ValueError:
        print("Invalid input")


# ================= MENU =================

while True:
    print("\n===== BANK SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Account")
    print("5. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            show_account()
        elif choice == 5:
            print("Thank You")
            break
        else:
            print("Invalid Choice")

    except ValueError:
        print("Enter number only")

conn.close()
