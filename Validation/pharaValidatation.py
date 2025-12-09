import re
def validate_medicine_name(name:str):
    if not name:
        raise Exception("medicine name cannot be empty")
    pattern= r"^[A-Za-z0-9\s]{3,50}$"
    if not re.match(pattern,name):
        raise Exception("Invalid medicine name!.. only letter,number, and spaces are allowed.")
    return True