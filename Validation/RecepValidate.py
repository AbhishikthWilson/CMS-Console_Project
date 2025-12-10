import re

def validate_name(value: str):
    if not value:
        raise Exception("Name cannot be empty")

    pattern = r"^[A-Za-z ]{3,50}$"
    if not re.fullmatch(pattern, value):
        raise Exception("Invalid name. Only alphabets and spaces allowed")
    return True


def validate_phone(value: str):
    if value:
        pattern = r"^\d{10}$"
        if not re.fullmatch(pattern, value):
            raise Exception("Invalid phone number. Must be 10 digits starting with 6-9")
        if value == '0000000000':
            raise Exception("Phone number cannot be all zeros.")
    return True


def validate_email(value: str):
    if value:
        pattern = r"^[A-Za-z0-9._%+-]+@gmail\.com$"
        if not re.fullmatch(pattern, value):
            raise Exception("Invalid email. Enter valid Gmail address")
    return True


def validate_role_id(value):
    if value is None:
        raise Exception("Role ID cannot be empty")
    try:
        value = int(value)
    except:
        raise Exception("Role ID must be a number")

    if value not in [1, 2, 3, 4]:
        raise Exception("Invalid role ID. 1-Admin, 2-Receptionist, 3-Doctor, 4-Pharmacist")
    return True
