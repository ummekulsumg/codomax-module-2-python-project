"""
Smart Expense Tracker
Codomax AI & ML Internship - Module 2

A beginner-friendly command-line application for
managing and analyzing personal expenses.
"""

from datetime import datetime


# -------------------------------------------------
# Expense Storage
# -------------------------------------------------

expenses = []


# -------------------------------------------------
# Utility Functions
# -------------------------------------------------

def display_header(title):
    """Display a formatted section header."""
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def get_positive_amount():
    """Get a valid positive expense amount from the user."""

    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


# -------------------------------------------------
# Add Expense
# -------------------------------------------------

def add_expense():
    """Add a new expense to the tracker."""

    display_header("ADD EXPENSE")

    category = input("Enter category: ").strip().title()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter description: ").strip()

    if not description:
        print("Description cannot be empty.")
        return

    amount = get_positive_amount()

    expense = {
        "category": category,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)

    print("\nExpense added successfully! ✓")


# -------------------------------------------------
# View Expenses
# -------------------------------------------------

def view_expenses():
    """Display all recorded expenses."""

    display_header("ALL EXPENSES")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print(
        f"{'No.':<5}"
        f"{'Date':<15}"
        f"{'Category':<18}"
        f"{'Description':<20}"
        f"{'Amount':>10}"
    )

    print("-" * 68)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<18}"
            f"{expense['description']:<20}"
            f"₹{expense['amount']:>8.2f}"
        )


# -------------------------------------------------
# Calculate Total
# -------------------------------------------------

def calculate_total():
    """Calculate and display the total expenses."""

    display_header("TOTAL EXPENSES")

    if not expenses:
        print("No expenses recorded yet.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total expenses: ₹{total:.2f}")


# -------------------------------------------------
# View Expenses by Category
# -------------------------------------------------

def view_by_category():
    """Display the total amount spent in each category."""

    display_header("EXPENSES BY CATEGORY")

    if not expenses:
        print("No expenses recorded yet.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    for category, total in sorted(category_totals.items()):
        print(f"{category:<25} ₹{total:.2f}")


# -------------------------------------------------
# Delete Expense
# -------------------------------------------------

def delete_expense():
    """Delete an expense using its number."""

    display_header("DELETE EXPENSE")

    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses()

    while True:
        try:
            choice = int(input("\nEnter expense number to delete: "))

            if choice < 1 or choice > len(expenses):
                print("Please enter a valid expense number.")
                continue

            removed_expense = expenses.pop(choice - 1)

            print(
                f"\nDeleted: {removed_expense['description']} "
                f"(₹{removed_expense['amount']:.2f}) ✓"
            )

            break

        except ValueError:
            print("Please enter a valid number.")


# -------------------------------------------------
# Main Menu
# -------------------------------------------------

def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 50)
    print("           SMART EXPENSE TRACKER")
    print("=" * 50)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. View By Category")
    print("5. Delete Expense")
    print("6. Exit")


# -------------------------------------------------
# Main Program
# -------------------------------------------------

def main():
    """Run the Smart Expense Tracker application."""

    print("\nWelcome to Smart Expense Tracker!")

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            view_by_category()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("\nThank you for using Smart Expense Tracker!")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please select a number from 1 to 6.")


# -------------------------------------------------
# Program Entry Point
# -------------------------------------------------

if __name__ == "__main__":
    main()