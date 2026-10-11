"""
test_expense_tracker.py
-----------------------
Unit tests for the Personal Expense Tracker backend.
Each test method resets the in-memory store to ensure isolation.
"""

import unittest
import sys
import os

# Ensure the project root is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.expense_tracker import (
    add_expense,
    get_all_expenses,
    calculate_total_expenses,
    filter_expenses_by_category,
    delete_expense,
    reset,
)


class TestAddExpense(unittest.TestCase):
    """Tests for add_expense()."""

    def setUp(self):
        reset()

    # --- Valid input ---

    def test_add_valid_expense_returns_dict(self):
        """Adding a valid expense should return a dictionary with the correct fields."""
        expense = add_expense("Lunch", 150.0, "Food", "2024-03-15")
        self.assertIsInstance(expense, dict)
        self.assertEqual(expense["description"], "Lunch")
        self.assertAlmostEqual(expense["amount"], 150.0)
        self.assertEqual(expense["category"], "Food")
        self.assertEqual(expense["date"], "2024-03-15")
        self.assertIn("id", expense)

    def test_add_expense_assigns_unique_ids(self):
        """Each expense should receive a unique auto-incremented ID."""
        e1 = add_expense("Bus ticket", 20.0, "Travel", "2024-03-10")
        e2 = add_expense("Coffee", 60.0, "Food", "2024-03-11")
        self.assertNotEqual(e1["id"], e2["id"])

    def test_add_expense_strips_whitespace(self):
        """Leading/trailing whitespace in description and category should be stripped."""
        expense = add_expense("  Dinner  ", 300.0, "  Food  ", "2024-03-12")
        self.assertEqual(expense["description"], "Dinner")
        self.assertEqual(expense["category"], "Food")

    def test_add_expense_rounds_amount_to_two_decimals(self):
        """Amount should be stored rounded to two decimal places."""
        expense = add_expense("Item", 99.999, "Shopping", "2024-04-01")
        self.assertEqual(expense["amount"], 100.0)

    # --- Invalid amount ---

    def test_add_expense_rejects_zero_amount(self):
        """Amount of zero should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Taxi", 0, "Travel", "2024-03-15")

    def test_add_expense_rejects_negative_amount(self):
        """Negative amount should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Taxi", -50.0, "Travel", "2024-03-15")

    def test_add_expense_rejects_non_numeric_amount(self):
        """Non-numeric amount should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Taxi", "abc", "Travel", "2024-03-15")

    # --- Invalid description ---

    def test_add_expense_rejects_empty_description(self):
        """Empty description should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("", 100.0, "Food", "2024-03-15")

    def test_add_expense_rejects_whitespace_only_description(self):
        """Whitespace-only description should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("   ", 100.0, "Food", "2024-03-15")

    # --- Invalid category ---

    def test_add_expense_rejects_empty_category(self):
        """Empty category should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "", "2024-03-15")

    def test_add_expense_rejects_whitespace_only_category(self):
        """Whitespace-only category should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "   ", "2024-03-15")

    # --- Invalid date ---

    def test_add_expense_rejects_invalid_date_format(self):
        """Date not in YYYY-MM-DD format should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "Food", "15-03-2024")

    def test_add_expense_rejects_invalid_month(self):
        """Month value 00 or > 12 should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "Food", "2024-13-01")


class TestGetAllExpenses(unittest.TestCase):
    """Tests for get_all_expenses()."""

    def setUp(self):
        reset()

    def test_get_all_expenses_empty_list(self):
        """Should return an empty list when no expenses exist."""
        self.assertEqual(get_all_expenses(), [])

    def test_get_all_expenses_returns_all_added(self):
        """Should return all added expenses."""
        add_expense("Lunch", 100.0, "Food", "2024-03-15")
        add_expense("Bus", 30.0, "Travel", "2024-03-16")
        expenses = get_all_expenses()
        self.assertEqual(len(expenses), 2)

    def test_get_all_expenses_returns_copy(self):
        """Modifying the returned list should not affect internal state."""
        add_expense("Lunch", 100.0, "Food", "2024-03-15")
        expenses = get_all_expenses()
        expenses.clear()
        self.assertEqual(len(get_all_expenses()), 1)


class TestCalculateTotalExpenses(unittest.TestCase):
    """Tests for calculate_total_expenses()."""

    def setUp(self):
        reset()

    def test_total_when_no_expenses(self):
        """Total of an empty list should be 0.0."""
        self.assertEqual(calculate_total_expenses(), 0.0)

    def test_total_single_expense(self):
        """Total of a single expense equals its amount."""
        add_expense("Lunch", 150.0, "Food", "2024-03-15")
        self.assertAlmostEqual(calculate_total_expenses(), 150.0)

    def test_total_multiple_expenses(self):
        """Total should be the sum of all expense amounts."""
        add_expense("Lunch", 100.0, "Food", "2024-03-15")
        add_expense("Bus", 30.0, "Travel", "2024-03-16")
        add_expense("Book", 250.0, "Education", "2024-03-17")
        self.assertAlmostEqual(calculate_total_expenses(), 380.0)


class TestFilterExpensesByCategory(unittest.TestCase):
    """Tests for filter_expenses_by_category()."""

    def setUp(self):
        reset()
        add_expense("Lunch", 100.0, "Food", "2024-03-15")
        add_expense("Dinner", 200.0, "Food", "2024-03-16")
        add_expense("Bus ticket", 30.0, "Travel", "2024-03-17")

    def test_filter_returns_matching_expenses(self):
        """Should return only expenses in the requested category."""
        results = filter_expenses_by_category("Food")
        self.assertEqual(len(results), 2)
        for expense in results:
            self.assertEqual(expense["category"], "Food")

    def test_filter_is_case_insensitive(self):
        """Category filter should be case-insensitive."""
        results = filter_expenses_by_category("food")
        self.assertEqual(len(results), 2)

    def test_filter_nonexistent_category_returns_empty(self):
        """Filtering by a category with no matches should return an empty list."""
        results = filter_expenses_by_category("Shopping")
        self.assertEqual(results, [])

    def test_filter_empty_category_raises(self):
        """Empty category string should raise ValueError."""
        with self.assertRaises(ValueError):
            filter_expenses_by_category("")

    def test_filter_returns_single_match(self):
        """Should return exactly one result for a category with one expense."""
        results = filter_expenses_by_category("Travel")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["description"], "Bus ticket")


class TestDeleteExpense(unittest.TestCase):
    """Tests for delete_expense()."""

    def setUp(self):
        reset()
        self.expense = add_expense("Lunch", 100.0, "Food", "2024-03-15")

    def test_delete_existing_expense(self):
        """Deleting a valid ID should remove the expense and return it."""
        deleted = delete_expense(self.expense["id"])
        self.assertEqual(deleted["id"], self.expense["id"])
        self.assertEqual(len(get_all_expenses()), 0)

    def test_delete_removes_correct_expense(self):
        """Only the targeted expense should be removed; others remain."""
        e2 = add_expense("Bus", 30.0, "Travel", "2024-03-16")
        delete_expense(self.expense["id"])
        remaining = get_all_expenses()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]["id"], e2["id"])

    def test_delete_nonexistent_id_raises(self):
        """Deleting a non-existent ID should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense(9999)

    def test_delete_invalid_id_zero_raises(self):
        """ID of zero should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense(0)

    def test_delete_negative_id_raises(self):
        """Negative ID should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense(-1)


if __name__ == "__main__":
    unittest.main()
