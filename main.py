import pandas as pd

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

# Check if the user wants to input transactions
if n > 0:
    # Create an instance of the ExpenseTracker class
    tracker = ExpenseTracker(user_name)

    # Input transactions
    for _ in range(n):
        date = input("Enter date: ")
        description = input("Enter description: ")
        category = input("Enter Category: ")
        amount = input("Enter your amount: ")

        # Add the transaction to the tracker
        tracker.add_transaction(date, description, category, amount)

    # Display all transactions
    tracker.display_transactions()
else:
    print("No transactions entered.")

