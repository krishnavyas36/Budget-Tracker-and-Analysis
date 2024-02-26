import tkinter as tk
from main import ExpenseTracker

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("1100x700")  # Set desired size

        # Create two frames for buttons
        self.frame1 = tk.Frame(self, pady=100)  # Add padding
        self.frame1.pack()

        # Button for "Add Transaction"
        self.add_button = tk.Button(self.frame1, text="Add Transaction", command=self.open_second_window, width=15, height=10)
        self.add_button.pack(side="left", padx=20)

        # Button for "See Transaction" (not implemented yet)
        self.see_button = tk.Button(self.frame1, text="See Transaction", command=self.placeholder, width=15, height=10)
        self.see_button.pack(side="right", padx=20)

    def open_second_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.grab_set()  # Make second window modal
        self.withdraw()  # Hide the main window

    def placeholder(self):
        print("See Transaction functionality not implemented yet.")


class SecondWindow(tk.Toplevel):
    def __init__(self, main_app):
        super().__init__(main_app)
        self.title("Add Transaction")
        self.geometry(main_app.geometry())  # Inherit geometry from main window

        # Input fields and labels
        self.date_entry = tk.Entry(self)
        self.username_entry = tk.Entry(self)
        self.category_entry = tk.Entry(self)
        self.amount_entry = tk.Entry(self)
        self.comments_entry = tk.Entry(self)

        self.date_label = tk.Label(self, text="Date")
        self.username_label = tk.Label(self, text="Username")
        self.category_label = tk.Label(self, text="Category")
        self.amount_label = tk.Label(self, text="Amount")
        self.comments_label = tk.Label(self, text="Comments (Optional)")

        # Layout elements using grid
        self.date_label.grid(row=0, column=0, sticky="W", padx=10, pady=5)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        self.username_label.grid(row=1, column=0, sticky="W", padx=10, pady=5)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.category_label.grid(row=2, column=0, sticky="W", padx=10, pady=5)
        self.category_entry.grid(row=2, column=1, padx=10, pady=5)

        self.amount_label.grid(row=3, column=0, sticky="W", padx=10, pady=5)
        self.amount_entry.grid(row=3, column=1, padx=10, pady=5)

        self.comments_label.grid(row=4, column=0, sticky="W", padx=10, pady=5)
        self.comments_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5)  # Span across 2 columns

        # Additional buttons and their functionality
        self.save_button = tk.Button(self, text="Save Transaction", command=self.save_data)
        self.save_button.grid(row=5, column=0, padx=10, pady=10)

        self.cancel_button = tk.Button(self, text="Go To Home", command=self.close_window)
        self.cancel_button.grid(row=5, column=1, padx=10, pady=10)

    def save_data(self):
        data = [
        self.date_entry.get(),
        self.username_entry.get(),
        self.category_entry.get(),
        self.amount_entry.get(),
        self.comments_entry.get()
    ]

    # Validate and process data if needed (optional)

        print("Added Transaction Data:")
        for item in data:
         print(f"- {item}")
        # ExpenseTracker.add_transaction(data[1],data[0],data[4],data[2],data[3])
        # ExpenseTracker.save_to_excel()
    # Clear all entry fields after saving
        self.date_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.comments_entry.delete(0, tk.END)

    def close_window(self):
            self.date_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.comments_entry.delete(0, tk.END)

    # Switch back to the main window
            self.master.deiconify()  # Shows the main window
            self.destroy()

# **Main Module:**
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()  # Start the event loop
