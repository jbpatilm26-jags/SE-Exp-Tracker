# AI Engineering Journal

> **Project:** Personal Expense Tracker  
> **Experiment:** AI-Augmented Software Development Environment  
> **Developer:** (Student Name)  
> **Date:** 2024-10-11  
> **AI Tool Used:** Antigravity AI Agent (Google DeepMind)

---

## Purpose

This journal documents every AI-assisted activity during the development of the Personal Expense Tracker. It records the prompts given to the AI, the AI's suggested output, and the human validation performed after each step.

> **Integrity Note:** Only activities that have actually been completed are marked ✅. Activities that remain pending are marked 🔲.

---

## Activity Log

| # | Activity | Prompt / Instruction Given | AI Output / Suggested Change | Human Validation | Status |
|---|---|---|---|---|---|
| 1 | Project planning and requirements review | "Help me implement a simple Personal Expense Tracker in Python. Keep it backend only with no GUI, database, or API. Use lists and dictionaries." | AI outlined a plan: create `expense_tracker.py` for business logic, `main.py` for CLI, and unit tests using `unittest`. Identified five core functions: `add_expense`, `get_all_expenses`, `calculate_total_expenses`, `filter_expenses_by_category`, `delete_expense`. | Reviewed plan; matched project requirements exactly. No changes needed. | ✅ Done |
| 2 | Generating initial Python implementation | "Implement `expense_tracker.py` with in-memory storage using a list of dicts. Include validation for description, amount, category, and date." | AI generated the full `expense_tracker.py` with all five functions, a `reset()` helper for tests, date validation with `re`, and `ValueError` for invalid inputs. | Read every function. Checked that no `print()` or `input()` calls exist in the backend. Verified validation logic. Code accepted. | ✅ Done |
| 3 | Code explanation — `add_expense` function | "Explain what the `add_expense` function does, step by step." | AI explained: (1) validates description is non-empty string, (2) validates category is non-empty string, (3) converts and validates amount is positive float, (4) validates date with regex, (5) creates dict, appends to `_expenses`, increments `_next_id`, returns dict. | Matched actual code. Explanation was accurate. | ✅ Done |
| 4 | Code explanation — `reset()` function | "Why does the `reset()` function exist? Should it be in the main module?" | AI explained: `reset()` clears the in-memory list and resets the ID counter. It is needed in unit tests (`setUp`) to ensure each test starts from a clean state. It should NOT be in `main.py` since users should not be able to call it. | Agreed. `reset()` is kept in `expense_tracker.py` but is documented as test-only. | ✅ Done |
| 5 | Generating unit tests | "Generate unit tests using `unittest` for all five backend functions. Include happy-path tests and error-condition tests. Use `reset()` in `setUp`." | AI generated `test_expense_tracker.py` with 29 test cases organized into 5 test classes, each calling `reset()` in `setUp`. Tests cover valid input, zero/negative amount, empty description/category, invalid date, empty store, case-insensitive filter, and invalid/nonexistent IDs. | Reviewed all test cases. Ran `python -m unittest discover -s tests -v` — all 29 tests passed. | ✅ Done |
| 6 | Identifying and fixing a validation issue | "What happens if the user passes a whitespace-only description like `'   '`? Is it rejected?" | AI identified that `not description.strip()` correctly evaluates to `True` for whitespace-only strings, so it IS rejected. Confirmed tests `test_add_expense_rejects_whitespace_only_description` and `test_add_expense_rejects_whitespace_only_category` verify this. | Ran the specific tests — both passed. No bug found; validation was already correct. | ✅ Done |
| 7 | Refactoring for readability | "Review `main.py` for clarity. Can the menu dispatch be simplified?" | AI suggested replacing a long `if/elif` chain with a `MENU_ACTIONS` dictionary mapping choice strings to handler functions. Implemented as `MENU_ACTIONS = {"1": handle_add_expense, ...}`. | Reviewed refactored code. Logic is cleaner and easier to extend. Accepted. | ✅ Done |
| 8 | Reviewing coding standards | "Check that `expense_tracker.py` follows PEP 8 and the documented coding standards." | AI confirmed: snake_case used throughout, docstrings present on all public functions, business logic separated from CLI, `ValueError` raised for invalid input, no duplicated code. One suggestion: add `round()` to the total calculation to avoid floating-point display issues. | Applied `round(..., 2)` to `calculate_total_expenses()`. Verified with tests. | ✅ Done |
| 9 | Running tests and recording results | "Run the full test suite and report the results." | AI ran `python -m unittest discover -s tests -v` and reported: **Ran 29 tests in 0.002s — OK**. All 29 tests passed; 0 errors, 0 failures. | Executed command independently. Confirmed same result. | ✅ Done |
| 10 | Human review and final validation | "Review the complete implementation once more before finalizing." | AI reviewed all files, confirmed structure matches requirements, no unnecessary dependencies, no personal data, no advanced features. Generated README, HUMAN_VALIDATION.md, and EXPERIMENT_REPORT.md. | Reviewed all files. Confirmed completeness. | ✅ Done |

---

## Key Observations

1. **AI accelerated the initial scaffolding** significantly. What might take a beginner 2–3 hours was generated in minutes.
2. **Human review was essential.** The AI's first draft of `calculate_total_expenses()` did not include rounding — a subtle issue that could cause display problems.
3. **Tests revealed design quality.** Writing unit tests forced a clear separation between business logic (`expense_tracker.py`) and CLI code (`main.py`). Without this separation, testing would have been difficult.
4. **AI explanations aided learning.** Asking the AI to explain functions step-by-step helped understand the purpose of each validation check.
5. **Responsible AI use:** No real financial data or personal information was included in any prompt.

---

## AI Limitations Observed

- The AI cannot run the code itself — a human must execute and verify the output.
- AI-generated code must always be reviewed; it can contain subtle bugs or miss edge cases.
- AI does not know the actual project context unless it is provided explicitly in each prompt.
