from Validation.RecepValidate import validate_patient_name
from datetime import date
    
class Medicine:
    """Medicine class oops applied here"""

    def __init__(self, medicine_id=None, medicine_name=None, category=None,
                 company_name=None, quantity=None, price=None,
                 expiry_date=None, created_on=None):

        self.__medicine_id = medicine_id
        self.__medicine_name = medicine_name
        self.__category = category
        self.__company_name = company_name
        self.__quantity = quantity
        self.__price = price
        self.__expiry_date = expiry_date
        self.__created_on = created_on

    @property
    def medicine_id(self):
        return self.__medicine_id

    @property
    def medicine_name(self):
        return self.__medicine_name

    @property
    def category(self):
        return self.__category

    @property
    def company_name(self):
        return self.__company_name

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    @property
    def expiry_date(self):
        return self.__expiry_date

    @property
    def created_on(self):
        return self.__created_on


    @medicine_id.setter
    def medicine_id(self, value):
        self.__medicine_id = value

    @medicine_name.setter
    def medicine_name(self, value):
        self.__medicine_name = value

    @category.setter
    def category(self, value):
        self.__category = value

    @company_name.setter
    def company_name(self, value):
        self.__company_name = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @price.setter
    def price(self, value):
        self.__price = value

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    @created_on.setter
    def created_on(self, value):
        self.__created_on = value

    def __str__(self):
        return (f'Medicine ID: {self.__medicine_id}, '
                f'Medicine Name: {self.__medicine_name}, '
                f'Category: {self.__category}, '
                f'Company: {self.__company_name}, '
                f'Quantity: {self.__quantity}, '
                f'Price: {self.__price}, '
                f'Expiry Date: {self.__expiry_date}, '
                f'Created On: {self.__created_on}')
    