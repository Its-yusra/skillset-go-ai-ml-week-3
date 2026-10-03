# Task 3.4 — AI-Assisted CSV Data Validator

## 1. Project Objective

Build a simple Python application that checks a CSV file for common data quality issues.

## 2. Functional Requirements

The application must:

1. Load a CSV file from a given file path.
2. Check whether required columns exist: `name`, `email`, and `age`.
3. Count missing values in each column.
4. Count duplicate rows.
5. Display a readable validation report.
6. Handle invalid file paths, empty files, and missing required columns appropriately.

## 3. Technical Requirements

* Programming language: Python
* Use Python's built-in `csv` module.
* Keep the code simple and readable.
* Separate validation logic from the command-line interface.
* Include automated tests.
* Do not use passwords, API keys, or other secrets.

## 4. Testing Requirements

Test a valid CSV file, missing required columns, an invalid file path, and an empty file.

## 5. Deliverables

* Working Python application
* Automated tests
* Test results
* AI-assisted coding audit notes
## 6. How to Run

Make sure Python is installed.

Run the application:

```bash
python app.py
```

Enter the CSV file path when prompted. For the included sample dataset, enter `sample_data.csv`.

## 7. How to Test

Run the automated tests:

```bash
python -m unittest -v test_app.py
```

## 8. Dependencies

The application uses Python's standard library. No additional packages are required.

## 9. Verification

See `test_results.txt` for the actual test output and `AI_AUDIT_NOTES.md` for the code review and audit record.
