import csv
import operator
from django.core.files.uploadedfile import UploadedFile

def perform_calculations(file: UploadedFile) -> float:
    if not file.name.lower().endswith('.csv'):
        raise ValueError("Invalid file format. Please upload a .csv file.")

    try:
        lines = file.read().decode('utf-8').splitlines()
        if not lines:
            raise ValueError("The file is empty.")

        first_line = lines[0]
        if ',' in first_line:
            delimiter = ','
        elif '|' in first_line:
            delimiter = '|'
        elif ';' in first_line:
            delimiter = ';'
        elif '\t' in first_line:
            delimiter = '\t'
        else:
            raise ValueError("Unsupported delimiter. Please use ',', '|', ';', or '\\t'.")

        csv_reader = csv.reader(lines, delimiter=delimiter)

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        total = 0

        for idx, row in enumerate(csv_reader):
            if not any(row):
                continue

            try:
                a = float(row[0])
                o = row[1]
                b = float(row[2])

                if o not in operations:
                    raise ValueError(f"Unsupported operator: {o}")

                result = operations[o](a, b)
                total += result
            except ZeroDivisionError:
                raise ValueError(f"Division by zero in row {idx + 1}")
            except Exception as e:
                raise ValueError(f"Error processing row {idx + 1}: {e}")

        return total

    except Exception as e:
        raise ValueError(f"Error processing file: {e}")
