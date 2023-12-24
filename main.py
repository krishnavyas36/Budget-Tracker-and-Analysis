import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self, user_name):
        # Initialize an empty DataFrame to store transactions
        self.user_name = user_name
        self.transactions = pd.DataFrame(columns=['User', 'Date', 'Description', 'Category', 'Amount'])

    def add_transaction(self, date, description, category, amount):
        # Add a new transaction to the DataFrame
        new_transaction = pd.DataFrame([[self.user_name, date, description, category, amount]],
                                       columns=['User', 'Date', 'Description', 'Category', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

    def display_transactions(self):
        # Display the current list of transactions
        print(self.transactions)

# Example usage:
user_name = input("Enter your name: ")
n = int(input("Enter the number of transactions to input: "))

# Define allowed categories
allowed_categories = ['Food', 'Entertainment', 'Transportation', 'Utilities', 'Other']

# Check if the user wants to input transactions
if n > 0:
    # Create an instance of the ExpenseTracker class
    tracker = ExpenseTracker(user_name)

    # Input transactions
    for _ in range(n):
        date_option = input("Enter 'C' for custom date or 'T' for today's date: ").upper()

        if date_option == 'C':
            date = input("Enter date (dd-mm-yyyy): ")
        elif date_option == 'T':
            date = datetime.now().strftime('%d-%m-%Y')
        else:
            print("Invalid option. Using today's date.")
            date = datetime.now().strftime('%d-%m-%Y')

        description = input("Enter description: ")

        # Input category with validation
        while True:
            category = input("Enter Category (Food/Entertainment/Transportation/Utilities/Other): ").capitalize()
            if category in allowed_categories:
                break
            else:
                print("Invalid category. Please choose from the allowed categories.")

        # Input amount with validation
        while True:
            amount_str = input("Enter your amount: ")
            if amount_str.isdigit():
                break
            else:
                print("Invalid amount. Please enter a numerical value.")

        amount = float(amount_str)

        # Add the transaction to the tracker
        tracker.add_transaction(date, description, category, amount)

    # Display all transactions
    tracker.display_transactions()
else:
    print("No transactions entered.")

