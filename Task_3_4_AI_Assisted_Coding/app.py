
import csv
from pathlib import Path


def validate_csv(file_path: str) -> dict:
    """Validate a CSV file and return a summary report."""

    path = Path(file_path)

    # Check whether the file exists and is a file
    if not path.is_file():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        # Check whether the file is empty or has no header
        if reader.fieldnames is None:
            raise ValueError("The CSV file is empty or has no header.")

        columns = reader.fieldnames

        required_columns = ["name", "email", "age"]
        missing_required_columns = [
            column
            for column in required_columns
            if column not in columns
        ]

        missing_value_counts = {column: 0 for column in columns}
        duplicate_rows = 0
        total_rows = 0
        seen_rows = set()

        for row in reader:
            total_rows += 1

            # Count missing values in each column
            for column in columns:
                value = row.get(column)
                if value is None or value.strip() == "":
                    missing_value_counts[column] += 1

            # Count duplicate data rows
            row_values = tuple(row.get(column) for column in columns)

            if row_values in seen_rows:
                duplicate_rows += 1
            else:
                seen_rows.add(row_values)

    return {
        "column_names": columns,
        "missing_required_columns": missing_required_columns,
        "missing_value_counts": missing_value_counts,
        "duplicate_row_count": duplicate_rows,
        "total_data_rows": total_rows,
    }


def main() -> None:
    """Ask for a CSV path and display its validation report."""

    file_path = input("Enter the CSV file path: ").strip()

    try:
        report = validate_csv(file_path)

        print("\n--- CSV Validation Report ---")
        print(f"Column names: {report['column_names']}")
        print(
            "Missing required columns: "
            f"{report['missing_required_columns']}"
        )
        print("Missing values per column:")

        for column, count in report["missing_value_counts"].items():
            print(f"  {column}: {count}")

        print(f"Duplicate rows: {report['duplicate_row_count']}")
        print(f"Total data rows: {report['total_data_rows']}")

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()