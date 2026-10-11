"""
expense_tracker.py
------------------
Core backend logic for the Personal Expense Tracker.
Expenses are stored in memory as a list of dictionaries.
No file I/O or database is used.
"""

import re

# In-memory store for all expenses
_expenses: list[dict] = []
_next_id: int = 1


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _is_valid_date(date_str: str) -> bool:
    """Return True if *date_str* matches YYYY-MM-DD format with valid values."""
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_str))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def add_expense(description: str, amount: float, category: str, date: str) -> dict:
    """Add a new expense and return it.

    Args:
        description: Non-empty text describing the expense.
        amount:      Positive monetary value.
        category:    Non-empty category label (e.g. "Food", "Travel").
        date:        Date string in YYYY-MM-DD format.

    Returns:
        The newly created expense dictionary.

    Raises:
        ValueError: If any input fails validation.
    """
    global _next_id

    if not isinstance(description, str) or not description.strip():
        raise ValueError("Description must be a non-empty string.")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be a non-empty string.")
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a number.")
    if amount <= 0:
        raise ValueError("Amount must be a positive number.")
    if not _is_valid_date(date):
        raise ValueError("Date must be in YYYY-MM-DD format (e.g. 2024-01-31).")

    expense = {
        "id": _next_id,
        "description": description.strip(),
        "amount": round(amount, 2),
        "category": category.strip(),
        "date": date,
    }
    _expenses.append(expense)
    _next_id += 1
    return expense


def get_all_expenses() -> list[dict]:
    """Return a copy of all recorded expenses."""
    return list(_expenses)


def calculate_total_expenses() -> float:
    """Return the sum of all expense amounts.  Returns 0.0 for an empty list."""
    return round(sum(e["amount"] for e in _expenses), 2)


def filter_expenses_by_category(category: str) -> list[dict]:
    """Return expenses whose category matches *category* (case-insensitive).

    Args:
        category: Category label to search for.

    Returns:
        List of matching expense dictionaries (may be empty).

    Raises:
        ValueError: If *category* is empty.
    """
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category filter must be a non-empty string.")
    target = category.strip().lower()
    return [e for e in _expenses if e["category"].lower() == target]


def delete_expense(expense_id: int) -> dict:
    """Delete the expense with the given *expense_id* and return it.

    Args:
        expense_id: Integer ID of the expense to remove.

    Returns:
        The deleted expense dictionary.

    Raises:
        ValueError: If *expense_id* is not a positive integer or not found.
    """
    if not isinstance(expense_id, int) or expense_id <= 0:
        raise ValueError("Expense ID must be a positive integer.")
    for i, expense in enumerate(_expenses):
        if expense["id"] == expense_id:
            return _expenses.pop(i)
    raise ValueError(f"No expense found with ID {expense_id}.")


def reset() -> None:
    """Clear all expenses and reset the ID counter.

    Intended for use in unit tests only.
    """
    global _next_id
    _expenses.clear()
    _next_id = 1
