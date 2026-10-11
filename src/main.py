"""
main.py
-------
Command-line interface for the Personal Expense Tracker.
Calls backend functions from expense_tracker.py.
"""

import sys
import os

# Allow running as  python src/main.py  from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.expense_tracker import (
    add_expense,
    get_all_expenses,
    calculate_total_expenses,
    filter_expenses_by_category,
    delete_expense,
)


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def _print_separator():
    print("-" * 52)


def _print_expense(expense: dict):
    print(
        f"  [{expense['id']:>3}] {expense['description']:<20} "
        f"Rs {expense['amount']:>8.2f}  "
        f"{expense['category']:<12} {expense['date']}"
    )


def _print_menu():
    _print_separator()
    print("       Personal Expense Tracker")
    _print_separator()
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Calculate Total Expenses")
    print("  4. Filter Expenses by Category")
    print("  5. Delete an Expense")
    print("  6. Exit")
    _print_separator()


# ---------------------------------------------------------------------------
# Feature handlers
# ---------------------------------------------------------------------------

def handle_add_expense():
    """Prompt user for expense details and call add_expense()."""
    print("\n-- Add Expense --")
    description = input("  Description : ").strip()
    amount_str = input("  Amount (Rs) : ").strip()
    category = input("  Category    : ").strip()
    date = input("  Date (YYYY-MM-DD): ").strip()

    try:
        amount = float(amount_str)
    except ValueError:
        print("  [ERROR] Invalid amount. Please enter a numeric value.")
        return

    try:
        expense = add_expense(description, amount, category, date)
        print(f"  [OK] Expense added with ID {expense['id']}.")
    except ValueError as err:
        print(f"  [ERROR] {err}")


def handle_view_expenses():
    """Display all recorded expenses."""
    print("\n-- All Expenses --")
    expenses = get_all_expenses()
    if not expenses:
        print("  No expenses recorded yet.")
        return
    _print_separator()
    print(f"  {'ID':>4}  {'Description':<20} {'Amount':>10}  {'Category':<12} Date")
    _print_separator()
    for expense in expenses:
        _print_expense(expense)
    _print_separator()


def handle_total_expenses():
    """Display the sum of all expense amounts."""
    total = calculate_total_expenses()
    print(f"\n  Total Expenses: Rs {total:.2f}")


def handle_filter_expenses():
    """Prompt for a category and display matching expenses."""
    print("\n-- Filter by Category --")
    category = input("  Enter category: ").strip()
    try:
        results = filter_expenses_by_category(category)
    except ValueError as err:
        print(f"  [ERROR] {err}")
        return

    if not results:
        print(f"  No expenses found for category '{category}'.")
        return

    _print_separator()
    print(f"  Expenses in category '{category}':")
    _print_separator()
    for expense in results:
        _print_expense(expense)
    _print_separator()


def handle_delete_expense():
    """Prompt for an expense ID and delete it."""
    print("\n-- Delete Expense --")
    id_str = input("  Enter Expense ID to delete: ").strip()
    try:
        expense_id = int(id_str)
    except ValueError:
        print("  [ERROR] ID must be a whole number.")
        return

    try:
        deleted = delete_expense(expense_id)
        print(f"  [OK] Deleted expense: '{deleted['description']}' (ID {deleted['id']}).")
    except ValueError as err:
        print(f"  [ERROR] {err}")


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

MENU_ACTIONS = {
    "1": handle_add_expense,
    "2": handle_view_expenses,
    "3": handle_total_expenses,
    "4": handle_filter_expenses,
    "5": handle_delete_expense,
}


def main():
    """Entry point: display menu and dispatch user choices."""
    print("\nWelcome to the Personal Expense Tracker!")
    while True:
        _print_menu()
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\n  Goodbye! Your expense data will not be saved.\n")
            break
        elif choice in MENU_ACTIONS:
            MENU_ACTIONS[choice]()
        else:
            print("  [ERROR] Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
