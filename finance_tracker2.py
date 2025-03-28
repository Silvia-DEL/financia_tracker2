# Personal Finance Tracker - Created by Silvia Mue

# Dictionary to store transactions
finance_data = {
    "income": [],  # List for income
    "expenses": []  # List for expenses
}

from datetime import datetime  # Import datetime to record the date

def add_transaction(transaction_type):
    amount = float(input("Enter the amount: "))  # Convert input to a number
    category = input("Enter the category (e.g., Salary, Food, Rent): ")
    description = input("Enter a short description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Save the date

    transaction = (amount, category, description, date)  # Save as a tuple

    if transaction_type == "income":
        finance_data["income"].append(transaction)  # Store in income
    else:
        finance_data["expenses"].append(transaction)  # Store in expenses

   print(f"{transaction_type.capitalize()} added successfully!")  # Confirmation

def view_summary():
    total_income = sum(i[0] for i in finance_data["income"])  # Add all income
    total_expenses = sum(e[0] for e in finance_data["expenses"])  # Add all expenses
    balance = total_income - total_expenses  # Calculate balance

    print("\n--- Financial Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${balance:.2f}")
    
import csv  # Import CSV module

def save_to_csv():
    with open("finance_tracker.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction Type", "Amount", "Category", "Description", "Date"])  # Column headers

        for income in finance_data["income"]:
            writer.writerow(["Income", *income])  # Write income transactions
        for expense in finance_data["expenses"]:
            writer.writerow(["Expense", *expense])  # Write expenses

    print("Transactions saved to finance_tracker.csv successfully!")   


def menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save to CSV")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expenses")
        elif choice == "3":
            view_summary()
        elif choice == "4":
            save_to_csv()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()    