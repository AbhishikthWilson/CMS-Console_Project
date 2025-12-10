import re
from datetime import datetime

def validate_medicine_name(name: str):
    if not name.strip():
        raise Exception("Medicine name cannot be empty.")
    pattern = r"^[A-Za-z0-9\s\-]{3,50}$"
    if not re.match(pattern, name):
        raise Exception("Invalid name! Only letters, numbers, spaces, hyphens allowed (3–50 chars).")
    return name.strip()

def validate_category(category: str):
    if not category.strip():
        raise Exception("Category cannot be empty.")
    pattern = r"^[A-Za-z\s]{3,30}$"
    if not re.match(pattern, category):
        raise Exception("Invalid category! Only letters and spaces allowed (min 3 chars).")
    return category.strip()

def validate_company_name(company: str):
    if not company.strip():
        raise Exception("Company name cannot be empty.")
    pattern = r"^[A-Za-z0-9\s\.\-]{2,50}$"
    if not re.match(pattern, company):
        raise Exception("Invalid company name! Only letters, numbers, spaces, dots, hyphens allowed.")
    return company.strip()

def validate_quantity(qty: str):
    if not qty.isdigit():
        raise Exception("Quantity must be a positive integer.")
    qty = int(qty)
    if qty <= 0:
        raise Exception("Quantity must be greater than 0.")
    return qty

def validate_price(price: str):
    try:
        p = float(price)
    except:
        raise Exception("Price must be a valid number.")
    if p <= 0:
        raise Exception("Price must be greater than 0.")
    return p

from datetime import datetime

def validate_expiry_date(date_str: str):
    try:
        # Convert DD/MM/YYYY → date object
        date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        raise Exception("Invalid date format! Use DD/MM/YYYY.")

    # Today's date
    today = datetime.today().date()

    # Expiry date must be **strictly greater** than today's date
    if date_obj <= today:
        raise Exception("Expiry date must be a future date.")

    # Convert to MySQL format → YYYY-MM-DD
    return date_obj.strftime("%Y-%m-%d")

