# Lab 6 – Code and Branch Coverage Analysis

## 1. Objective

To understand code coverage and branch coverage, measure test coverage using Python tools, identify untested code paths, and improve test cases to achieve at least 90% code coverage and branch coverage.

## 2. Project Description

This project focuses on testing a food delivery application that calculates delivery charges based on distance, order value, and weather conditions, applies coupon codes, and estimates delivery time based on peak hours and restaurant workload.

## 3. Technologies Used

- Python 3
- `pytest` – Testing framework
- `coverage.py` – Code and branch coverage measurement tool

## 4. Files Included

| File Name | Description |
|---|---|
| `food_delivery.py` | Application code containing delivery charge, coupon, and delivery time functions |
| `CodeCoverageTest_20_food_delivery.py` | Test cases for code coverage analysis |
| `BranchCoverageTest_20_food_delivery.py` | Test cases for branch coverage analysis |
| `code_coverage.png` | Screenshot of code coverage results |
| `branch_coverage.png` | Screenshot of branch coverage results |

## 5. Installation

Install the required Python packages using:

```bash
pip install coverage pytest
```

## 6. Running the Tests

### 6.1 Code Coverage

Run the following commands to measure statement coverage:

```bash
coverage erase
coverage run -m pytest CodeCoverageTest_20_food_delivery.py
coverage report -m
```

### 6.2 Branch Coverage

Run the following commands to measure statement and branch coverage:

```bash
coverage erase
coverage run --branch -m pytest BranchCoverageTest_20_food_delivery.py
coverage report -m
```

## 7. Test Coverage Results

The test suite contains 22 test cases, and all tests passed successfully.

| Metric | Result |
|---|---:|
| Total test cases | 22 |
| Tests passed | 22 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Total branches measured | 24 |
| Partial branches | 0 |
| Missed application statements | 0 |

## 8. Functionalities Tested

### 8.1 Delivery Charge Calculation

- Small and large order values
- Different delivery distance ranges
- Additional charges during rain
- Invalid delivery distances
- Maximum permitted delivery distance

### 8.2 Coupon Application

- Orders without coupons
- Valid `SAVE50` and `WELCOME` coupons
- Invalid coupon codes
- First-order coupon restrictions
- Minimum order value conditions

### 8.3 Delivery Time Estimation

- Normal delivery conditions
- Peak-hour delays
- Busy restaurant delays
- Combined peak-hour and restaurant delays
- Zero-distance input

## 9. Screenshots

The following screenshots document the coverage results:

- `code_coverage.png` – Code coverage report showing 100% statement coverage.
- `branch_coverage.png` – Branch coverage report showing 100% coverage, 24 branches, and 0 partial branches.

## 10. Conclusion

The food delivery application was tested using `pytest` and `coverage.py`. All 22 test cases passed successfully. The final reports showed 100% statement coverage and 100% branch coverage, with no missed application statements or partial branches.

The lab demonstrates how systematic test cases can be used to verify application logic and improve test coverage.
