# Lab 5: Static Code Analysis — Reflection Answers

### 1. What did you learn about static code analysis?

I learned that static code analysis examines source code without executing it to identify potential bugs, security vulnerabilities, and coding-style violations. Pylint, Bandit, and Flake8 provide different perspectives on code quality.

### 2. What issues did you identify and fix?

Pylint identified issues including missing docstrings, long lines, inconsistent naming, a mutable default argument, and a global statement. Bandit identified a potentially unsafe SQL query constructed using string formatting and unnecessary shell execution. Flake8 identified line-length violations and an incorrect comparison with `None`. I corrected the relevant issues and reran the tools to verify the changes.

### 3. How did static analysis improve your program?

Static analysis helped make the program more readable and maintainable. Parameterized SQL queries reduced the risk of SQL injection, while replacing the mutable default argument avoided sharing a list between function calls. Formatting and documentation improvements made the code easier to understand.

### 4. What challenges did you face?

One challenge was understanding that each tool detects a different category of issue. I had to inspect the reports, identify the underlying causes, modify the code, and rerun the tools to verify the results.

### 5. What did you learn about the limitations of static analysis?

Static analysis tools can identify suspicious patterns, but their findings still require human judgment. A clean report does not guarantee that a program is completely secure or free of logical errors, so testing and code review remain important.
