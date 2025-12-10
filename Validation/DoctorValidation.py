# File: Validation/DoctorValidation.py

import re

# ---------------------- INTEGER VALIDATION ----------------------

def validate_int(prompt, field_name):
    """Validate positive integer inputs (IDs, quantity, etc.)"""
    while True:
        value = input(prompt).strip()

        if value.isdigit() and int(value) > 0:
            return int(value)

        print(f"{field_name} must be a *positive* number.\n")


# ---------------------- NON EMPTY TEXT ----------------------

def validate_non_empty(prompt, field_name):
    """Validate non-empty input"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"{field_name} cannot be empty.\n")


# ---------------------- DOSAGE VALIDATION ----------------------

def validate_dosage():
    """
    Valid dosage formats:
    - 500mg
    - 250 mg
    - 1 tablet
    - 2 tablets
    - 5 ml
    - 1 capsule
    """
    pattern = r"^\d+\s*(mg|ml|tablet[s]?|capsule[s]?)$"

    while True:
        dosage = input("Enter Dosage (Ex: 500mg / 1 tablet / 5 ml): ").strip().lower()

        if re.match(pattern, dosage):
            return dosage

        print("Invalid dosage format! Example: 500mg, 1 tablet, 5 ml.\n")


# ---------------------- FREQUENCY VALIDATION ----------------------

def validate_frequency():
    """
    Valid frequency formats:
    - 1-0-1
    - 1-1-1
    - 0-0-1
    - once daily
    - twice daily
    - thrice daily
    - before food / after food
    """
    pattern_numeric = r"^\d-\d-\d$"
    allowed_text = [
        "once daily", "twice daily", "thrice daily",
        "before food", "after food", "at bedtime"
    ]

    while True:
        frequency = input(
            "Enter Frequency (Ex: 1-0-1 / once daily / after food): "
        ).strip().lower()

        if re.match(pattern_numeric, frequency) or frequency in allowed_text:
            return frequency

        print("Invalid frequency! Examples: 1-0-1, once daily, after food.\n")


# ---------------------- DURATION VALIDATION ----------------------

def validate_duration():
    """
    Valid duration formats:
    - 5 days
    - 7 days
    - 1 week
    - 2 weeks
    - 3 days
    """
    pattern = r"^\d+\s*(day[s]?|week[s]?)$"

    while True:
        duration = input("Enter Duration (Ex: 5 days / 1 week): ").strip().lower()

        if re.match(pattern, duration):
            return duration

        print("Invalid duration! Example: 5 days, 1 week.\n")
