# Experiment Report

## AI-Augmented Software Development Environment Using a Personal Expense Tracker

---

### Experiment Title
AI-Augmented Software Development Environment

### Aim
To demonstrate how an AI coding assistant can support the complete software development lifecycle — from requirements analysis and code generation to testing, debugging, refactoring, and documentation — while maintaining human oversight at every step.

### Objectives
1. Use an AI coding assistant to generate Python backend code for a Personal Expense Tracker.
2. Validate, review, and correct all AI-generated code as a human developer.
3. Write and run unit tests using Python's `unittest` framework.
4. Apply PEP 8 coding standards throughout the project.
5. Maintain a detailed AI Engineering Journal to document the human-AI collaboration.
6. Use Git and GitHub for version control and project submission.

---

### Problem Statement
Manually writing all code for a software project is time-consuming and error-prone. AI coding assistants can generate initial implementations quickly, but they require human supervision to ensure correctness, security, and maintainability. This experiment investigates how a developer can effectively collaborate with an AI tool to build a simple, well-tested Python application.

---

### Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Programming language |
| `unittest` | Built-in testing framework |
| Git | Local version control |
| GitHub | Remote repository hosting |
| VS Code | Code editor |
| Antigravity AI Agent | AI coding assistant (Google DeepMind) |
| Ruff / Black (optional) | Linting and formatting |

---

### Project Structure

```
personal-expense-tracker/
├── src/
│   ├── __init__.py
│   ├── expense_tracker.py   ← business logic
│   └── main.py              ← command-line interface
├── tests/
│   ├── __init__.py
│   └── test_expense_tracker.py
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

### Implementation Methodology

Development followed a structured AI-augmented workflow:

1. **Requirements Review** — The project specification was provided to the AI assistant, which outlined a plan including five core backend functions and a CLI layer.
2. **Code Generation** — The AI generated `expense_tracker.py` with full validation logic and `main.py` with a menu-driven CLI.
3. **Human Review** — Every line of AI-generated code was read and understood by the human developer.
4. **Testing** — The AI generated 29 unit tests. The human ran them and confirmed all passed.
5. **Bug Identification** — Human review identified a missing `round()` call in `calculate_total_expenses()`. The AI confirmed the fix.
6. **Refactoring** — The AI suggested replacing an `if/elif` chain with a dispatch dictionary in `main.py` for cleaner code.
7. **Documentation** — README, coding standards, AI journal, and this report were written with AI assistance and human review.

---

### AI-Assisted Development Activities

| Activity | AI Role | Human Role |
|---|---|---|
| Planning | Outlined project structure and functions | Verified alignment with requirements |
| Code generation | Generated `expense_tracker.py` and `main.py` | Reviewed every function; accepted with one fix |
| Code explanation | Explained `add_expense()` and `reset()` step by step | Confirmed accuracy against code |
| Test generation | Generated 29 unit tests | Ran tests; confirmed all passed |
| Bug finding | Confirmed validation logic was correct for whitespace | Ran specific tests to verify |
| Refactoring | Suggested dispatch-dict pattern for menu | Reviewed and accepted |
| Standards review | Checked PEP 8 compliance; suggested `round()` | Applied `round()` fix; verified |
| Documentation | Generated README, journal, checklist, report | Reviewed all documents for accuracy |

---

### Unit Testing and Results

Tests were written using Python's built-in `unittest` module and organized into five test classes:

| Test Class | Functions Tested | Test Count |
|---|---|---|
| `TestAddExpense` | `add_expense()` | 13 |
| `TestGetAllExpenses` | `get_all_expenses()` | 3 |
| `TestCalculateTotalExpenses` | `calculate_total_expenses()` | 3 |
| `TestFilterExpensesByCategory` | `filter_expenses_by_category()` | 5 |
| `TestDeleteExpense` | `delete_expense()` | 5 |
| **Total** | | **29** |

**Command used:**
```bash
python -m unittest discover -s tests -v
```

**Actual result:**
```
Ran 29 tests in 0.002s

OK
```

All 29 tests passed. Zero failures. Zero errors.

---

### Human Validation and Review

A complete Human Validation Checklist was maintained in `docs/HUMAN_VALIDATION.md`. Key validation steps:

- All six menu options tested manually.
- All validation rules (empty input, zero/negative amounts, invalid dates) confirmed.
- Invalid menu choices confirmed to not crash the program.
- Unit test suite confirmed to pass with no failures.
- Code reviewed for PEP 8 compliance.
- No real financial data or personal information used anywhere.

---

### Git and Version Control Workflow

1. Initialized local Git repository in the project directory.
2. Created `.gitignore` to exclude `__pycache__`, `.pyc` files, and editor metadata.
3. Staged all project files using `git add .`.
4. Committed with a descriptive message: `git commit -m "Initial commit: Personal Expense Tracker"`.
5. Linked to GitHub remote: `git remote add origin https://github.com/jbpatilm26-jags/SE-Exp-Tracker.git`.
6. Pushed to the `main` branch: `git push -u origin main`.

---

### Security, Privacy, and Responsible AI Considerations

- **No real data:** No actual expense records, personal names, or financial information were used at any stage.
- **No secrets:** No API keys, passwords, or tokens appear in any file.
- **Human oversight:** Every AI suggestion was reviewed before use. The AI did not have autonomous write access to the repository.
- **Transparency:** The AI Engineering Journal accurately records what the AI suggested and what the human changed.
- **No fabrication:** Test results and validation steps are based on actual execution, not assumed outcomes.

---

### Conclusion

This experiment demonstrated that AI coding assistants significantly accelerate software development while requiring active human participation. The AI generated a correct, well-structured Python backend in a fraction of the time it would take manually. However, human review was essential — it caught a rounding issue and ensured the design met the project requirements. The combination of AI generation and human validation produced a clean, tested, and well-documented codebase that adheres to PEP 8 standards.

---

## Answers to Viva Questions

**1. What is an AI-augmented software development environment?**  
An AI-augmented software development environment is one where AI tools assist developers during the coding process. These tools can generate code, explain existing code, suggest bug fixes, write tests, and produce documentation. In this project, Antigravity AI Agent was used to generate the initial Python implementation, unit tests, and documentation. The human developer reviewed and validated all AI output before accepting it.

**2. Why is Git or version control important in software development?**  
Git tracks every change made to the codebase over time. It allows developers to see what changed, when, and why; revert to a previous version if something breaks; collaborate with others without overwriting each other's work; and maintain a clear history of the project. In this project, Git was used to commit changes after each development phase, giving a traceable record of how the Personal Expense Tracker evolved.

**3. What is an AI coding assistant?**  
An AI coding assistant is a software tool that uses a large language model (LLM) to help developers write, understand, and improve code. It can generate functions from a description, explain what existing code does, suggest refactoring improvements, and create unit tests. Examples include GitHub Copilot, Antigravity AI Agent, and ChatGPT. These tools work best when the developer provides clear context and reviews all suggestions critically.

**4. What is repository context, and why is it useful?**  
Repository context refers to the existing files, structure, coding conventions, and history present in a project repository. When an AI coding assistant is given access to repository context, it can generate code that matches the project's style, uses the correct module names, and follows established patterns. In this project, providing the `copilot-instructions.md` file gave the AI assistant context about the project constraints (backend only, no database, standard library only), resulting in more relevant and accurate suggestions.

**5. What is an AI engineering journal?**  
An AI engineering journal is a document that records every interaction between a developer and an AI coding assistant during a project. It captures the prompts given, the AI's suggestions, what the human accepted or changed, and the final status of each activity. The journal ensures transparency, helps the developer reflect on the AI's usefulness and limitations, and provides evidence for academic or professional review. In this project, the journal is stored in `docs/AI_ENGINEERING_JOURNAL.md`.

**6. Why should developers review AI-generated code?**  
AI coding assistants can generate plausible-looking code that contains subtle bugs, uses incorrect logic, violates security best practices, or does not meet the project's specific requirements. In this project, human review identified a missing `round()` call in `calculate_total_expenses()` that the AI had not included. Without review, this error could have caused floating-point display issues. Developers must treat AI output as a starting point that requires verification, not as a finished product.

**7. How can coding standards be enforced in a project?**  
Coding standards can be enforced by documenting rules in a standards file (such as `config/coding_standards.md`), performing code reviews, using automated linting tools like Ruff to detect violations, and using formatters like Black to automatically fix style issues. In this project, PEP 8 was the baseline standard. The AI was instructed to follow it, and the human reviewer checked each file for compliance before accepting it.

**8. Why is unit testing important?**  
Unit tests verify that individual functions behave correctly in isolation. They catch bugs early, make it safe to refactor code (since tests confirm that behaviour has not changed), and serve as live documentation of how functions are expected to work. In this project, 29 unit tests covering all five backend functions were written and run. They confirmed that validation for empty inputs, zero amounts, invalid dates, and missing IDs all worked correctly.

**9. What information should never be shared with an AI coding assistant?**  
Developers should never share: real passwords, API keys, or authentication tokens; personal financial data or bank account information; private medical or personal records; confidential business logic, trade secrets, or proprietary algorithms; personally identifiable information (PII) such as names, addresses, or phone numbers. In this project, all prompts used only fictional, generic data (e.g. "Lunch, Rs 100, Food, 2024-03-15").

**10. How does repository context improve AI-generated code?**  
When an AI assistant knows the project structure, naming conventions, constraints, and existing code, it generates suggestions that fit naturally into the existing codebase. Without context, the AI might suggest a database, a web framework, or a class-based design that contradicts the project requirements. In this project, the `copilot-instructions.md` file told the AI to use only the standard library, keep code backend-only, and follow the naming conventions already established in `expense_tracker.py`. This resulted in generated code that integrated cleanly without requiring major rewrites.
