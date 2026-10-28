Lab 5: Static Code Analysis — Scholarship Disbursement

Student: Pravith Mohandas
SRN: PES1UG24AM202
Repository: L5_20_scholarship_disbursement
Tools: Pylint, Bandit, Flake8

1. Static Analysis Tools

Tool

Purpose

Initial Result

Final Result

Pylint

Code quality, naming, documentation, and potential programming errors

5.00/10

9.69/10

Bandit

Detection of potentially insecure Python coding patterns

4 findings across 3 warning types

No issues identified

Flake8

Python formatting and PEP 8 style checks

6 reported violations

No reported violations

2. Issue Identification and Resolution

No.

Issue

Tool / Code

Severity

Description

Fix Applied

Status

1

Missing module docstring

Pylint C0114

Convention

Module lacked documentation.

Added module-level docstring.

Fixed

2

Missing function docstrings

Pylint C0116

Convention

Functions lacked descriptions.

Added descriptive function docstrings.

Fixed

3

Mutable default argument

Pylint W0102

Warning

audit=[] could share mutable state between calls.

Changed default to None and initialized the list inside the function.

Fixed

4

SQL injection risk

Bandit B608

Medium

SQL INSERT statement used string formatting.

Replaced string interpolation with parameterized SQL placeholders.

Fixed

5

Shell execution

Bandit B605, B607

Low

os.system() invoked a shell command unnecessarily.

Replaced shell execution with Python's print() function and removed the unused os import.

Fixed

6

Silent exception handling

Bandit B110, Pylint W0718

Low / Warning

Broad exception was caught and ignored using pass.

Removed the unnecessary shell command and exception handler.

Fixed

7

Long lines

Pylint C0301, Flake8 E501

Convention

Statements exceeded the configured line-length limits.

Reformatted statements across multiple lines.

Fixed

8

Invalid naming conventions

Pylint C0103

Convention

Variable and function names did not follow Python naming conventions.

Renamed disbursed_total to DISBURSED_TOTAL and bySchemeCount to by_scheme_count.

Fixed

9

Comparison with None

Pylint C0121, Flake8 E711

Convention

Used scheme == None.

Changed to scheme is None.

Fixed

10

Inconsistent return statements

Pylint R1710

Warning

Function did not return a value on every execution path.

Added return None when the award does not exist.

Fixed

11

Global statement

Pylint W0603

Warning

disburse() modifies the global DISBURSED_TOTAL variable.

Identified in the report; the warning remains in the current version.

Remaining

3. Before-and-After Metrics

Metric

Before Fixes

After Fixes

Pylint score

5.00/10

9.69/10

Bandit total findings

4

0

Bandit medium-severity findings

1

0

Bandit low-severity findings

3

0

Flake8 reported violations

6

0

4. Git Commit History

No.

Commit Hash

Commit Message

Changes

1

3de6056

Fix Pylint code quality issues

Added corrected Python file and Pylint before-and-after reports.

2

ae02842

Fix and verify Bandit security issues

Added Bandit before-and-after reports.

3

e1ab782

Fix Flake8 issues and document findings

Added Flake8 before-and-after reports and issue documentation.
