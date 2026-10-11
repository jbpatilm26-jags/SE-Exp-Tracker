# Coding Standards

> Project: Personal Expense Tracker  
> Language: Python 3  
> Standard: PEP 8

---

## 1. General Rules

- Follow [PEP 8](https://peps.python.org/pep-0008/) for all Python code.
- Maximum line length: **79 characters**.
- Use **4 spaces** for indentation (no tabs).
- Separate top-level function definitions with **two blank lines**.
- Separate methods inside a class with **one blank line**.

---

## 2. Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Functions | `snake_case` | `add_expense()` |
| Variables | `snake_case` | `expense_id` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_DESCRIPTION_LEN` |
| Classes | `PascalCase` | `ExpenseTracker` |
| Modules | `snake_case` | `expense_tracker.py` |

Use **meaningful, self-documenting names**. Avoid single-letter variables except in short loops (`for i in ...`).

---

## 3. Functions

- Each function should have **one clear responsibility**.
- Keep functions **short** (ideally under 20 lines of body).
- Validate all function arguments at the top of the function.
- Raise `ValueError` with a descriptive message for invalid input.
- Return values rather than printing inside business-logic functions.

---

## 4. Docstrings

- Add a docstring to every public function and module.
- Use the **Args / Returns / Raises** format:

```python
def add_expense(description: str, amount: float, category: str, date: str) -> dict:
    """Add a new expense.

    Args:
        description: Non-empty text describing the expense.
        amount: Positive monetary value.
        category: Non-empty category label.
        date: Date string in YYYY-MM-DD format.

    Returns:
        The newly created expense dictionary.

    Raises:
        ValueError: If any input fails validation.
    """
```

---

## 5. Comments

- Write comments to explain **why**, not **what**.
- Avoid obvious comments such as `# increment counter`.
- Use `# ---` section dividers to group related functions inside a module.

---

## 6. Input Validation

- Validate all user-supplied values before use.
- Strip leading/trailing whitespace from string inputs.
- Reject empty strings, non-positive numbers, and malformed dates early.
- Raise `ValueError` with a clear message; never let invalid data silently enter the system.

---

## 7. Separation of Concerns

- **Business logic** lives in `src/expense_tracker.py` — no `input()` or `print()` calls here.
- **CLI interaction** lives in `src/main.py` — no business logic here; it only calls backend functions.
- **Tests** live in `tests/` — they import and test only the backend module.

---

## 8. Error Handling

- Use `try / except` blocks at the CLI layer to catch `ValueError` from the backend.
- Do not use bare `except:` clauses; always specify the exception type.
- Display a user-friendly error message; do not expose raw tracebacks to the user.

---

## 9. Code Duplication

- Extract repeated logic into a helper function rather than copy-pasting.
- Reuse display helpers (`_print_separator`, `_print_expense`) in `main.py`.

---

## 10. Testing

- Write unit tests for every public function.
- Each test method must call `reset()` in `setUp` to ensure test isolation.
- Test both the **happy path** and **error conditions**.
- Use descriptive test method names that explain what is being verified.

---

## 11. Optional Tools

If available in the environment, use the following tools (they are **not required** to run the project):

- **Ruff** — fast linting: `ruff check src/ tests/`
- **Black** — auto-formatting: `black src/ tests/`
