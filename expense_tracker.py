import csv
import os
from datetime import datetime
from tabulate import tabulate

EXPENSES_FILE = "expenses.csv"

if not os.path.exists(EXPENSES_FILE):
    with open(EXPENSES_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Category", "Amount"])


def add_expense():
    """Add a new expense."""
    date = datetime.now().strftime("%Y-%m-%d")
    description = input("Enter description: ").strip()
    category = input("Enter category (e.g., Food, Transport): ").strip()
    amount = float(input("Enter amount: ").strip())
    
    with open(EXPENSES_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])
    
    print("\nExpense added successfully!")


def view_expenses():
    with open(EXPENSES_FILE, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if len(rows) <= 1:
        print("\nNo expenses recorded yet.")
    else:
        print("\nAll Expenses:")
        print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))


def generate_report():
    total_expenses = 0
    category_totals = {}
    
    with open(EXPENSES_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            amount = float(row[3])
            total_expenses += amount
            category_totals[row[2]] = category_totals.get(row[2], 0) + amount
    
    print("\nExpense Summary:")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print("\nExpenses by Category:")
    for category, total in category_totals.items():
        print(f"  {category}: ${total:.2f}")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
