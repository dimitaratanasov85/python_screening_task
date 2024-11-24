import io
import pytest
from compute.utils import perform_calculations  
from django.core.files.uploadedfile import UploadedFile

def test_perform_calculations_valid_file():
    mock_csv_content = b"A|O|B\n1|+|2\n3|*|4\n5|-|6\n8|/|4"
    mock_file = io.BytesIO(mock_csv_content)
    mock_file.name = "test_file.csv"
    uploaded_file = UploadedFile(file=mock_file, name="test_file.csv")

    result = perform_calculations(uploaded_file)
    assert result == 3 + 12 - 1 + 2

def test_perform_calculations_invalid_file_format():
    mock_file = io.BytesIO(b"")
    mock_file.name = "test_file.txt"
    uploaded_file = UploadedFile(file=mock_file, name="test_file.txt")

    with pytest.raises(ValueError, match="Invalid file format"):
        perform_calculations(uploaded_file)

def test_perform_calculations_empty_file():
    mock_file = io.BytesIO(b"")
    mock_file.name = "test_file.csv"
    uploaded_file = UploadedFile(file=mock_file, name="test_file.csv")

    with pytest.raises(ValueError, match="The file is empty"):
        perform_calculations(uploaded_file)

def test_perform_calculations_unsupported_delimiter():
    mock_csv_content = b"A~O~B\n1~+~2"
    mock_file = io.BytesIO(mock_csv_content)
    mock_file.name = "test_file.csv"
    uploaded_file = UploadedFile(file=mock_file, name="test_file.csv")

    with pytest.raises(ValueError, match="Unsupported delimiter"):
        perform_calculations(uploaded_file)
