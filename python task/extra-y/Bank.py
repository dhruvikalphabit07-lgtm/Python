import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="bankdb"
)

cursor = conn.cursor()

def create_account():
    """
    For create account.
    """
    try:
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        if balance < 0:
            print("Balance cannot be negative")
            return

        cursor.execute(
            "INSERT INTO accounts (name, balance, created_date) VALUES (%s,%s,%s)",
            (name, balance, datetime.now()),
        )
        conn.commit()

        print("Account Created Successfully")
        print("Account Number:", cursor.lastrowid)

    except ValueError:
        print("Invalid input")


def deposit():
    """
    For deposit money.
    """
    try:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))

        cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
        result = cursor.fetchone()

        if not result:
            print("Account not found")
            return

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_no=%s",
            (amount, acc_no),
        )

        cursor.execute(
            "INSERT INTO transactions (account_no, type, amount, date) VALUES (%s,%s,%s,%s)",
            (acc_no, "Deposit", amount, datetime.now()),
        )

        conn.commit()
        print("Deposit Successful")

    except ValueError:
        print("Invalid input")


def withdraw():
    """
    For withdraw money.
    """
    try:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdraw Amount: "))

        cursor.execute("SELECT balance FROM accounts WHERE account_no=%s", (acc_no,))
        result = cursor.fetchone()

        if not result:
            print("Account not found")
            return

        if result[0] < amount:
            print("Insufficient balance")
            return

        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_no=%s",
            (amount, acc_no),
        )

        cursor.execute(
            "INSERT INTO transactions (account_no, type, amount, date) VALUES (%s,%s,%s,%s)",
            (acc_no, "Withdraw", amount, datetime.now()),
        )

        conn.commit()
        print("Withdrawal Successful")

    except ValueError:
        print("Invalid input")


def account_details():
    """
    For fetch account details.
    """
    try:
        acc_no = int(input("Enter Account Number: "))

        cursor.execute("SELECT * FROM accounts WHERE account_no=%s", (acc_no,))
        acc = cursor.fetchone()

        if not acc:
            print("Account not found")
            return

        print("\nAccount Details")
        print("Account Number:", acc[0])
        print("Name:", acc[1])
        print("Balance:", acc[2])
        print("Created Date:", acc[3])

        cursor.execute(
            "SELECT account_no, type, amount, date FROM transactions WHERE account_no=%s",
            (acc_no,),
        )
        rows = cursor.fetchall()

        if rows:
            print("\nTransaction History")
            print("%-13s %-13s %-10s %-10s" % ("Account_No", "Type", "Amount", "Date"))
            for r in rows:
                print("%-13d %-13s %-10.2f %-10s" % (r[0], r[1], r[2], r[3]))
        else:
            print("\nNo transactions found")

    except ValueError:
        print("Invalid input")


def transfer():
    """
    For transfer money to other account.
    """
    try:
        acc_no = input("Enter your Account number: ")
        acc_no_transfer = input("Enter account number for transfer: ")
        transfer_amount = float(input("Enter Amount: "))

        cursor.execute("SELECT * FROM accounts WHERE account_no=%s", (acc_no,))
        acc = cursor.fetchone()

        if not acc:
            print("Account not found")
            return

        if acc[2] < transfer_amount:
            print("Balance is low in account number:", acc_no)
            return

        cursor.execute(
            "UPDATE accounts SET balance = balance - %s WHERE account_no=%s",
            (transfer_amount, acc_no),
        )

        cursor.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_no=%s",
            (transfer_amount, acc_no_transfer),
        )

        cursor.execute(
            "INSERT INTO transactions (account_no, type, amount, date) VALUES (%s,%s,%s,%s)",
            (acc_no, "Transfer", transfer_amount, datetime.now()),
        )

        cursor.execute(
            "INSERT INTO transactions (account_no, type, amount, date) VALUES (%s,%s,%s,%s)",
            (acc_no_transfer, "Deposit", transfer_amount, datetime.now()),
        )

        conn.commit()
        print("Transfer Successfully")

    except ValueError:
        print("Enter Valid input")


# ================= MENU =================

while True:

    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Account Details")
    print("5. Transfer Money")
    print("6. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            account_details()
        elif choice == 5:
            transfer()
        elif choice == 6:
            print("Thank you")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Enter number only")

conn.close()
