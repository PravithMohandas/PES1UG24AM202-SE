
# Lab 5: Static Code Analysis — Scholarship Disbursement

**Student:** Pravith Mohandas  
**SRN:** PES1UG24AM202  
**Repository:** `L5_20_scholarship_disbursement`  
**Tools:** Pylint, Bandit, Flake8

---

## 1. Objective

To improve Python code quality, security, readability, and maintainability using static code analysis tools. The scholarship disbursement program was analyzed using Pylint, Bandit, and Flake8 to identify and fix programming issues, potential security vulnerabilities, and coding-style violations.

## 2. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Programming language |
| Pylint | Checks code quality, naming conventions, documentation, and potential programming errors |
| Bandit | Detects potentially insecure Python coding patterns |
| Flake8 | Checks Python formatting and PEP 8 style conventions |
| SQLite3 | Provides the in-memory database for scholarship records |
| Git and GitHub | Version control and submission |

## 3. Project Structure

```text
LAB-5/
├── README.md
├── scholarship_disbursement.py
├── pylint_report.txt
├── pylint_after.txt
├── bandit_report.txt
├── bandit_after.txt
├── flake8_report.txt
├── flake8_after.txt
├── issue_table.md
└── reflection_answers.md
```

## 4. Program Functionality

The scholarship disbursement program implements the following operations:

- **Grant scholarships:** Records student, scheme, and amount information in the SQLite database.
- **Disburse scholarships:** Marks an award as disbursed and updates the total disbursed amount.
- **Count awards by scheme:** Returns the number of awards associated with a scholarship scheme.
- **Archive operation:** Prints a message indicating that archiving has been requested.

The database is created in memory using SQLite3.

## 5. Static Analysis Procedure

### Step 1: Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install the analysis tools

```bash
pip install pylint bandit flake8
```

### Step 3: Run the original program

```bash
python3 scholarship_disbursement.py
```

### Step 4: Generate the initial reports

```bash
pylint scholarship_disbursement.py > pylint_report.txt
bandit -r scholarship_disbursement.py > bandit_report.txt
flake8 scholarship_disbursement.py > flake8_report.txt
```

### Step 5: Fix the identified issues

The following improvements were made based on the reports:

- Added module and function docstrings.
- Replaced the mutable default argument with safe list initialization.
- Replaced SQL string formatting with parameterized queries.
- Removed unnecessary shell execution and silent exception handling.
- Improved variable and function naming conventions.
- Corrected comparisons with `None`.
- Reformatted long lines.
- Added a consistent return value for the unsuccessful disbursement path.

### Step 6: Generate the final reports

```bash
pylint scholarship_disbursement.py > pylint_after.txt 2>&1
bandit -r scholarship_disbursement.py > bandit_after.txt 2>&1
flake8 scholarship_disbursement.py > flake8_after.txt 2>&1
```

## 6. Before-and-After Results

| Metric | Initial Result | Final Result |
|---|---:|---:|
| Pylint score | 5.00/10 | 9.69/10 |
| Bandit findings | 4 | 0 |
| Flake8 reported violations | 6 | 0 |

**Note:** The final Pylint report still contains the `W0603` warning related to the use of a global statement. The final score exceeds the required target of 9.5/10.

## 7. Deliverables

| Deliverable | File |
|---|---|
| Corrected Python program | `scholarship_disbursement.py` |
| Initial Pylint report | `pylint_report.txt` |
| Final Pylint report | `pylint_after.txt` |
| Initial Bandit report | `bandit_report.txt` |
| Final Bandit report | `bandit_after.txt` |
| Initial Flake8 report | `flake8_report.txt` |
| Final Flake8 report | `flake8_after.txt` |
| Issue identification and resolution table | `issue_table.md` |
| Reflection answers | `reflection_answers.md` |

## 8. Git Commit History

| No. | Commit Hash | Commit Message |
|---:|---|---|
| 1 | `3de6056` | Fix Pylint code quality issues |
| 2 | `ae02842` | Fix and verify Bandit security issues |
| 3 | `e1ab782` | Fix Flake8 issues and document findings |

## 9. Conclusion

Static code analysis was performed on the scholarship disbursement program using Pylint, Bandit, and Flake8. The Pylint score improved from 5.00/10 to 9.69/10, Bandit reported no remaining findings, and Flake8 reported no remaining violations.

The process improved code readability, maintainability, and security. The remaining Pylint global-statement warning was documented for further improvement.
