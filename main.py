import pandas as pd
from datetime import datetime
from gui import get_data_on_submit
import uuid
import os

class ExpenseTracker:
    def __init__(self, user_name):
        # Initialize an empty DataFrame to store transactions
        self.user_name = user_name
        self.transactions = pd.DataFrame(columns=['TransactionID', 'User', 'Date', 'Description', 'Category', 'Amount'])

    def add_transaction(self, date, description, category, amount):
        # Generate a unique transaction ID using uuid
        transaction_id = str(uuid.uuid4())
        
        # Add a new transaction to the DataFrame with the generated ID
        new_transaction = pd.DataFrame([[transaction_id, self.user_name, date, description, category, amount]],
                                       columns=['TransactionID', 'User', 'Date', 'Description', 'Category', 'Amount'])
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

    def display_transactions(self):
        # Display the current list of transactions
        print(self.transactions)

    def save_to_excel(self, file_path='transactions.xlsx'):
        # Check if the file exists
        if os.path.exists(file_path):
            # If the file exists, read existing data
            existing_data = pd.read_excel(file_path)
            # Append new transactions to existing data
            updated_data = pd.concat([existing_data, self.transactions], ignore_index=True)
            # Save the updated data to the Excel file
            updated_data.to_excel(file_path, index=False)
        else:
            # If the file doesn't exist, save the current transactions to a new file
            self.transactions.to_excel(file_path, index=False)
    def load_from_excel(self, file_path='transactions.xlsx'):
        if os.path.exists(file_path):
            self.transactions = pd.read_excel(file_path)

    def filter_transactions(self, date=None, username=None, amount=None):
        filtered_transactions = self.transactions
        if date is not None:
            filtered_transactions = filtered_transactions[filtered_transactions['Date'] == date]
        if username is not None:
            filtered_transactions = filtered_transactions[filtered_transactions['User'] == username]
        if amount is not None:
            filtered_transactions = filtered_transactions[filtered_transactions['Amount'] == amount]
        return filtered_transactions
# Example usage:
# user_name = input("Enter your name: ")
# n = int(input("Enter the number of transactions to input: "))

# # Define allowed categories
# allowed_categories = ['Food', 'Entertainment', 'Transportation', 'Utilities', 'Other']

# # Check if the user wants to input transactions
# if n > 0:
#     # Create an instance of the ExpenseTracker class
#     tracker = ExpenseTracker(user_name)

#     # Input transactions
#     for _ in range(n):
#         date_option = input("Enter 'C' for custom date or 'T' for today's date: ").upper()

#         if date_option == 'C':
#             date = input("Enter date (dd-mm-yyyy): ")
#         elif date_option == 'T':
#             date = datetime.now().strftime('%d-%m-%Y')
#         else:
#             print("Invalid option. Using today's date.")
#             date = datetime.now().strftime('%d-%m-%Y')

#         description = input("Enter description: ")

#         # Input category with validation
#         while True:
#             category = input("Enter Category (Food/Entertainment/Transportation/Utilities/Other): ").capitalize()
#             if category in allowed_categories:
#                 break
#             else:
#                 category = "Other"

#         # Input amount with validation
#         while True:
#             amount_str = input("Enter your amount: ")
#             if amount_str.isdigit():
#                 break
#             else:
#                 print("Invalid amount. Please enter a numerical value.")

#         amount = float(amount_str)

#         # Add the transaction to the tracker
#         tracker.add_transaction(date, description, category, amount)

#     # Display all transactions
#     tracker.display_transactions()
# else:
#     print("No transactions entered.")

transactionToBeAdded = get_data_on_submit()
tracker = ExpenseTracker(transactionToBeAdded[0])
tracker.add_transaction(transactionToBeAdded[1],transactionToBeAdded[2],transactionToBeAdded[3],transactionToBeAdded[4])
tracker.display_transactions()
tracker.save_to_excel()
filtered = tracker.filter_transactions(date='2024-04-01', username='John', amount=50.0)
print("Filtered Transactions:")
print(filtered)