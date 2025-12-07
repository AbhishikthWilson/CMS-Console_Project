import re 

def validate_name(value:str):
    '''validate name
            --only alphabet,spaces allowed
            --length 3 to 50 characters
    '''
    if not value:
        raise Exception("product name cannot be empty")
    
    #Regex pattern
    pattern = r"^[A-Za-z\s]{3,50}$"
    if not re.match(pattern,value):
        raise Exception("invalid name."\
            "Only alphabets and spaces are allowed")
        
    return True

def validate_phone(value:str):
    pattern = r"^[0-9]{10}$"
    if value:
        if not re.match(pattern,value):
           raise Exception("invalid Phone number."\
            "Only 10 Digits are allowed")
        elif value == '0000000000':
            raise Exception("invalid Phone number."\
            "Phone number cannot be all zeros.")

    return True

def validate_email(value:str):
    pattern = r"^[A-Za-z0-9]+@gmail\.com$"

    if value:
        if not re.match(pattern,value):
           raise Exception("invalid Email."\
            "enter valid email")
    return True

def validate_role_id(value:int):
    if not value:
        raise Exception("role Id cannot be empty")
    
    role_id = [1,2,3,4]
    if value not in role_id:
        raise Exception("Invalid role id."\
            "1-Admin,2-Receptionist,3-Doctor,4-Pharmacist") 
    return True
