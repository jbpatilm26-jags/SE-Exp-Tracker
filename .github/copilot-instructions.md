# Copilot / AI Assistant Instructions

## Project Overview

This is a **Personal Expense Tracker** — a beginner-level Python backend project.  
It is part of a Software Engineering practical on AI-Augmented Development.

---

## Important Constraints

- **Backend only.** Do NOT suggest frontends, GUIs, APIs, databases, or web frameworks.
- **Standard library only.** Do NOT introduce third-party packages. The only allowed module beyond the standard library is used for optional linting/formatting (Ruff, Black).
- **Simple in-memory storage.** Expenses are stored as a list of dictionaries. No file I/O.
- **No advanced features.** No budgets, charts, authentication, multi-user support, or analytics.

---

## Project Structure

```
personal-expense-tracker/
├── src/
│   ├── __init__.py
│   ├── expense_tracker.py   ← business logic ONLY
│   └── main.py              ← CLI / user interaction ONLY
├── tests/
│   ├── __init__.py
│   └── test_expense_tracker.py
├── docs/
├── config/
│   └── coding_standards.md
└── README.md
```

---

## Coding Conventions

- Follow PEP 8.
- Use `snake_case` for functions and variables.
- Use `UPPER_SNAKE_CASE` for constants.
- Write docstrings in **Args / Returns / Raises** format.
- Raise `ValueError` for invalid user input; never silently accept bad data.
- Keep business logic in `expense_tracker.py` and CLI code in `main.py`.

---

## Running the Application

```bash
python src/main.py
```

---

## Running Tests

```bash
python -m unittest discover -s tests -v
```

Tests use `reset()` (defined in `expense_tracker.py`) in `setUp` to ensure isolation.

---

## Security Notes

- Do NOT include any real financial data, personal information, or secrets in prompts or code.
- Do NOT commit API keys, passwords, or credentials.
