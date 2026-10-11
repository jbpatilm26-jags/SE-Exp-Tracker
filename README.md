# Personal Expense Tracker

> A beginner-friendly Python backend application built as part of the Software Engineering practical on **AI-Augmented Software Development Environments**.

---

## Project Description

The Personal Expense Tracker is a simple command-line Python application that lets you record, view, filter, and delete personal expenses during a single program session. All data is stored in memory — no database or file I/O is used. The project demonstrates how AI coding assistants can support the full software development lifecycle under human supervision.

---

## Aim and Objectives

**Aim:** Demonstrate AI-augmented software development by building and testing a Personal Expense Tracker using Python and an AI coding assistant.

**Objectives:**
1. Generate backend Python code with AI assistance and validate it as a human developer.
2. Implement all required expense management features using only the Python standard library.
3. Write and run unit tests using `unittest`.
4. Apply PEP 8 coding standards throughout.
5. Document the AI-human collaboration process in an AI Engineering Journal.

---

## Features

| Feature | Description |
|---|---|
| Add Expense | Enter description, amount, category, and date. Input is validated. |
| View All Expenses | Display all expenses with ID, description, amount, category, and date. |
| Calculate Total | Show the sum of all recorded expense amounts. |
| Filter by Category | Display expenses belonging to a specific category (case-insensitive). |
| Delete an Expense | Remove an expense by its ID. |
| Menu-driven CLI | Text menu that runs until the user selects Exit. Invalid input does not crash the program. |

---

## Technologies Used

- **Python 3** — core language
- **`unittest`** — built-in testing framework (no extra packages needed)
- **Git + GitHub** — version control and remote repository
- **Antigravity AI Agent** — AI coding assistant used during development
- **VS Code** — code editor

---

## Repository Structure

```
personal-expense-tracker/
├── src/
│   ├── __init__.py
│   ├── expense_tracker.py   ← business logic (add, view, total, filter, delete)
│   └── main.py              ← command-line menu interface
├── tests/
│   ├── __init__.py
│   └── test_expense_tracker.py  ← 29 unit tests
├── docs/
│   ├── AI_ENGINEERING_JOURNAL.md
│   ├── HUMAN_VALIDATION.md
│   └── EXPERIMENT_REPORT.md
├── config/
│   └── coding_standards.md
├── .github/
│   └── copilot-instructions.md
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.8 or later
- No third-party packages required

To check your Python version:
```bash
python --version
```

---

## Running the Application

From the project root directory, run:

```bash
python src/main.py
```

---

## Running the Tests

From the project root directory, run:

```bash
python -m unittest discover -s tests -v
```

**Expected result:**
```
Ran 29 tests in 0.002s

OK
```

---

## Example Menu Interaction

```
Welcome to the Personal Expense Tracker!
----------------------------------------------------
       Personal Expense Tracker
----------------------------------------------------
  1. Add Expense
  2. View All Expenses
  3. Calculate Total Expenses
  4. Filter Expenses by Category
  5. Delete an Expense
  6. Exit
----------------------------------------------------
  Enter your choice (1-6): 1

-- Add Expense --
  Description : Lunch at canteen
  Amount (Rs) : 85
  Category    : Food
  Date (YYYY-MM-DD): 2024-03-15
  [OK] Expense added with ID 1.

  Enter your choice (1-6): 3

  Total Expenses: Rs 85.00

  Enter your choice (1-6): 6

  Goodbye! Your expense data will not be saved.
```

---

## Limitations

- **In-memory storage only.** All expense data is lost when the program exits. There is no file-based or database persistence.
- **Single user, single session.** The application does not support multiple users or saving data between sessions.
- **No budget tracking, charts, or analytics.** Only basic CRUD operations are implemented.
- **Command-line only.** There is no graphical user interface, web interface, or mobile app.

---

## How AI Assistance Was Used

The Antigravity AI Agent (Google DeepMind) was used to:

1. **Plan** the project structure and function signatures.
2. **Generate** the initial implementation of `expense_tracker.py` and `main.py`.
3. **Explain** key functions step by step.
4. **Generate** 29 unit tests in `tests/test_expense_tracker.py`.
5. **Suggest** a refactoring improvement (dispatch dictionary for the menu).
6. **Review** code for PEP 8 compliance and identify a missing `round()` call.
7. **Help write** documentation including the README, journal, and experiment report.

**All AI-generated code and documentation was reviewed, tested, and validated by a human developer before acceptance.** The Human Validation Checklist in `docs/HUMAN_VALIDATION.md` records the outcome of this review.

---

## GitHub Repository

[https://github.com/jbpatilm26-jags/SE-Exp-Tracker](https://github.com/jbpatilm26-jags/SE-Exp-Tracker)
