# Human Validation Checklist

> **Project:** Personal Expense Tracker  
> **Reviewer:** (Student Name)  
> **Date of Review:** 2024-10-11

---

## Instructions

Each item below must be verified by a human developer running and inspecting the actual code. Check an item only after you have personally confirmed it. Do not check an item you have not verified.

---

## Feature Verification

- [x] **Add Expense** — A valid expense (description, positive amount, non-empty category, YYYY-MM-DD date) is accepted and assigned a unique ID.
- [x] **View All Expenses** — All added expenses are displayed with ID, description, amount, category, and date.
- [x] **View with no expenses** — The message "No expenses recorded yet." is displayed when the list is empty.
- [x] **Calculate Total** — The correct sum of all expenses is displayed.
- [x] **Calculate Total (empty)** — Total shows `Rs 0.00` when no expenses exist.
- [x] **Filter by Category** — Only expenses matching the requested category are shown (case-insensitive).
- [x] **Filter non-existent category** — An appropriate "no expenses found" message is shown.
- [x] **Delete Expense** — An expense is correctly removed by its ID.
- [x] **Delete with invalid ID** — An appropriate error message is shown; the program does not crash.

---

## Input Validation

- [x] **Zero amount rejected** — Entering `0` for amount shows an error and does not add an expense.
- [x] **Negative amount rejected** — Entering `-50` for amount shows an error.
- [x] **Non-numeric amount rejected** — Entering `abc` for amount shows an error.
- [x] **Empty description rejected** — Leaving description blank shows an error.
- [x] **Whitespace-only description rejected** — Entering only spaces shows an error.
- [x] **Empty category rejected** — Leaving category blank shows an error.
- [x] **Invalid date format rejected** — Entering `15-03-2024` shows an error.

---

## CLI Behaviour

- [x] **Invalid menu choice** — Entering a letter or number outside 1–6 shows an error and redisplays the menu (no crash).
- [x] **Non-integer expense ID** — Entering `abc` as an ID to delete shows an error (no crash).
- [x] **Exit** — Selecting option 6 exits gracefully with a goodbye message.

---

## Unit Tests

- [x] **All tests pass** — `python -m unittest discover -s tests -v` reports **29 tests, 0 failures, 0 errors**.
- [x] **Tests are isolated** — Each test class calls `reset()` in `setUp`; tests do not share state.

---

## Code Quality

- [x] **PEP 8 compliance** — Code follows the rules in `config/coding_standards.md`.
- [x] **Docstrings present** — All public functions in `expense_tracker.py` have docstrings.
- [x] **Business logic separated** — `expense_tracker.py` contains no `input()` or `print()` calls.
- [x] **CLI separated** — `main.py` contains no business logic; it only calls backend functions.
- [x] **No unnecessary dependencies** — Only Python standard library modules are used.

---

## AI Code Review

- [x] **AI-generated code reviewed by human** — All code in `src/expense_tracker.py` and `src/main.py` was read line by line.
- [x] **Rounding fix applied** — `calculate_total_expenses()` uses `round(..., 2)` after human review identified the need.
- [x] **No fabricated content** — The AI Engineering Journal documents only activities that actually occurred.

---

## Security and Privacy

- [x] **No real financial data** — No actual expense records, bank details, or personal financial information were used in development or included in any file.
- [x] **No personal information** — No names, addresses, phone numbers, or other PII are stored in the codebase.
- [x] **No secrets committed** — No API keys, passwords, or tokens are in any file.
- [x] **No sensitive prompts** — AI prompts did not include any personal or confidential information.

---

## Items Requiring Manual Verification After Submission

> The following items should be checked by the student before final submission:

- [ ] Run `python src/main.py` and manually test all six menu options.
- [ ] Confirm the GitHub repository is accessible at the URL in README.md.
- [ ] Confirm `git log` shows meaningful commit messages.
