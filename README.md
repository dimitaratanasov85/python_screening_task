# python_screening_task
# CSV Calculator API

This project provides a REST API to upload a `.csv` file containing arithmetic operations and perform calculations row by row. The results are returned along with a request ID. The API uses token-based authentication to ensure secure access.

---

## Features
- Upload `.csv` files with arithmetic operations for calculation.
- Token-based authentication using JSON Web Tokens (JWT).
- Automatic handling of various delimiters (`|`, `,`, `;`, `\t`).
- Validation to ensure the integrity of uploaded files.
- Refresh tokens for secure and continuous access.

---

## Endpoints

### **1. `/api/compute/`**
**Description**: Accepts a `.csv` file, processes it, and returns the total result of calculations.
- **Method**: `POST`
- **Headers**:
  - `Authorization`: Bearer token (required)
- **Body**:
  - Form Data: key: "file"; value: <file_name>.csv
  - A file with `.csv` extension. The file should follow this format:
    ```
    A|O|B
    1|+|2
    3|*|4
    ```
    Where:
    - Column `A` and `B` are numeric operands.
    - Column `O` is the operator (`+`, `-`, `*`, `/`).
- **Response**:
  ```json
  {
      "request_id": "<unique_id>",
      "result": 16.0
  }

### **2. `/api/token/`**
**Description**: Generates a JWT token for authenticated access to the API.
- **Method**: `POST`
- **Body**:
  ```json
  {
      "username": "admin",
      "password": "admin"
  }
- **Response**:
  ```json
  {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
  }

### **3. `/api/token/refresh/`**
**Description**: Refreshes an expired JWT access token using a refresh token.
- **Method**: `POST`
- **Body**:
  ```json
  {
    "refresh": "<your_refresh_token>"
  }
- **Response**:
  ```json
  {
    "access": "<new_access_token>"
  }

##  Example Workflow
### **1. `Generate a token: Use /api/token/ to get your access and refresh tokens.`**
### **2. `Make a request: Send a .csv file to /api/compute/ with the Authorization: Bearer <access_token> header.`**
### **3. `Refresh your token: Use /api/token/refresh/ when your access token expires to obtain a new one.`**

##  Setup Instructions
### **1. `Clone the repository:`**
**git clone <repository_url>**
**cd <project_directory>**
### **2. `Install dependencies:`**
**pip install -r requirements.txt**
### **3. `Apply migrations:`**
**python manage.py migrate**
### **4. `Start the development server:`**
**python manage.py runserver**
### **5. `Create a superuser for authentication:`**
**python manage.py createsuperuser**
