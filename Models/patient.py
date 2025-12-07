from Validation.RecepValidate import validate_name,validate_email,validate_phone
from datetime import date 
    
class Patient:
    'Patient class oops applied here'
    def __init__(self,patient_id=None,first_name=None,last_name=None,gender=None,DOB=None,age=None,phone=None,address=None,email=None,created_on=None):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__DOB = DOB 
        self.__age = age
        self.__phone = phone
        self.__address = address
        self.__email = email
        self.__created_on = created_on
    
    @property
    def patient_id(self):
        return self.__patient_id
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def DOB(self):
        return self.__DOB
    
    @property
    def age(self):
        return self.__age
    
    @property
    def phone(self):
        return self.__phone
    
    @property
    def address(self):
        return self.__address
    
    @property
    def email(self):
        return self.__email 
    
    @property
    def created_on(self):
        return self.__created_on
    
    @patient_id.setter
    def patient_id(self,value):
        self.__patient_id= value
        
        
    @first_name.setter
    def first_name(self,value):
        try:
           validate_name(value)
           self.__first_name = value
        except Exception as e:
            print(f'Name validation error:{e}') 
            raise   
        
    @last_name.setter
    def last_name(self,value):
        try:
           validate_name(value)
           self.__last_name = value
        except Exception as e:
            print(f'Last_name validation error:{e}') 
            raise    
    
    @gender.setter
    def gender(self,value):
        self.__gender = value
    
    @DOB.setter
    def DOB(self,value):
        self.__DOB = value
    
    @age.setter
    def age(self,value):
        self.__age = value
    
    @phone.setter
    def phone(self,value):
        try:
           validate_phone(value)
           self.__phone= value
        except Exception as e:
            print(f'phone number validation error:{e}') 
            raise    
        
    @address.setter
    def address(self,value):
        self.__address= value 
        
    @email.setter
    def email(self,value):
        try:
           validate_email(value)
           self.__email= value
        except Exception as e:
            print(f'Email validation error:{e}') 
            raise
        
    
    @created_on.setter
    def created_on(self,value):
        self.__created_on = value        
            
        
    def __str__(self):
        return (f'patient id: {self.__patient_id},'
                f'first name: {self.__first_name},'
                f'last_name: {self.__last_name},'
                f'gender: {self.__gender},'
                f'Date of birth: {self.__DOB},'
                f'age: {self.__age},'
                f'phone: {self.__phone},'
                f'address: {self.__address},'
                f'email: {self.__email},'
                f'created_on: {self.__created_on},'
                ) 
         
    
     
    