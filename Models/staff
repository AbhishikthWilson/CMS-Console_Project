from Validation.RecepValidate import validate_name,validate_email,validate_phone,validate_role_id
from datetime import date

class Staff:
    """Staff class OOP applied here"""

    def __init__(self, staff_id=None, name=None, email=None,
                 phone=None, status=None, created_on=None, role_id=None):

        self.__staff_id = staff_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__status = status
        self.__created_on = created_on
        self.__role_id = role_id


    @property
    def staff_id(self):
        return self.__staff_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def phone(self):
        return self.__phone

    @property
    def status(self):
        return self.__status

    @property
    def created_on(self):
        return self.__created_on

    @property
    def role_id(self):
        return self.__role_id


    @staff_id.setter
    def staff_id(self, value):
        self.__staff_id = value

    @name.setter
    def name(self, value):
        try:
            validate_name(value)
            self.__name = value
        except Exception as e:
            print(f"Staff name validation error: {e}")
            raise

    @email.setter
    def email(self, value):
        try:
            validate_email(value)
            self.__email = value
        except Exception as e:
            print(f'Email validation error:{e}') 
            raise

    @phone.setter
    def phone(self, value):
        try:
           validate_phone(value)
           self.__phone= value
        except Exception as e:
            print(f'phone number validation error:{e}') 
            raise 

    @status.setter
    def status(self, value):
        self.__status = value

    @created_on.setter
    def created_on(self, value):
        self.__created_on = value

    @role_id.setter
    def role_id(self, value):
        try:
            validate_role_id(value)
            self.__role_id = value
        except Exception as e:
            print(f"Role ID validation error: {e}")
            raise

    def __str__(self):
        return (
            f"Staff ID: {self.__staff_id}, "
            f"Name: {self.__name}, "
            f"Email: {self.__email}, "
            f"Phone: {self.__phone}, "
            f"Status: {self.__status}, "
            f"Created On: {self.__created_on}, "
            f"Role ID: {self.__role_id}"
        )
