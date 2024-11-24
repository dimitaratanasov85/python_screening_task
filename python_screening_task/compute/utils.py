import csv
import operator
from typing import List, Optional
from django.core.files.uploadedfile import UploadedFile


def validate_file(file: UploadedFile) -> None:
    if not file.name.lower().endswith('.csv'):
        raise ValueError("Invalid file format. Please upload a .csv file.")


def detect_delimiter(first_line: str) -> str:
    for delimiter in [',', '|', ';', '\t']:
        if delimiter in first_line:
            return delimiter
    raise ValueError("Unsupported delimiter. Please use ',', '|', ';', or '\\t'.")


def parse_csv(file_content: str, delimiter: str) -> List[List[str]]:
    lines = file_content.splitlines()
    if not lines:
        raise ValueError("The file is empty.")
    return list(csv.reader(lines, delimiter=delimiter))


def is_numeric(value: str) -> bool:
    return value.replace('.', '', 1).isdigit()


def calculate_row(row: List[str], row_idx: int, operations: dict) -> Optional[float]:
    try:
        if not (is_numeric(row[0]) and is_numeric(row[2])):
            print(f"Skipping non-numeric row {row_idx}: {row}")
            return None

        a = float(row[0])
        o = row[1]
        b = float(row[2])

        if o not in operations:
            raise ValueError(f"Unsupported operator: {o}")

        return operations[o](a, b)

    except ZeroDivisionError:
        raise ValueError(f"Division by zero in row {row_idx}")
    except Exception as e:
        raise ValueError(f"Error processing row {row_idx}: {e}")


def perform_calculations(file: UploadedFile) -> float:
    validate_file(file)
    try:
        file_content = file.read().decode('utf-8')
        lines = file_content.splitlines()

        if not lines:
            raise ValueError("The file is empty.")

        delimiter = detect_delimiter(lines[0])
        rows = parse_csv(file_content, delimiter)

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }

        total = 0
        for idx, row in enumerate(rows, start=1):

            result = calculate_row(row, idx, operations)
            if result is not None:
                total += result

        return total

    except Exception as e:
        raise ValueError(f"Error processing file: {e}")
