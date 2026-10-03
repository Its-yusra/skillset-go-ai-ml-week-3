
import tempfile
import unittest
from pathlib import Path

from app import validate_csv


class TestCSVValidator(unittest.TestCase):

    def test_valid_sample_csv(self):
        result = validate_csv("sample_data.csv")

        self.assertEqual(result["total_data_rows"], 6)
        self.assertEqual(result["duplicate_row_count"], 1)
        self.assertEqual(result["missing_value_counts"]["email"], 1)
        self.assertEqual(result["missing_value_counts"]["age"], 1)
        self.assertEqual(result["missing_required_columns"], [])

    def test_missing_required_columns(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "missing_columns.csv"
            file_path.write_text(
                "name,city\nAli,Lahore\n",
                encoding="utf-8"
            )

            result = validate_csv(file_path)

            self.assertEqual(
                result["missing_required_columns"],
                ["email", "age"]
            )

    def test_invalid_file_path(self):
        with self.assertRaises(FileNotFoundError):
            validate_csv("file_that_does_not_exist.csv")

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "empty.csv"
            file_path.write_text("", encoding="utf-8")

            with self.assertRaises(ValueError):
                validate_csv(file_path)


if __name__ == "__main__":
    unittest.main()