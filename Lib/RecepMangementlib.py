from datetime import datetime
from Dao.AdminAbstract import AbstractDemo
from Dao.AdminAbstractImplementation import AbstractImplementation
from Models.patient import Patient

class RecepManagementLib:   
    """handles CRUD logic"""
    
    dao_service : AbstractDemo = AbstractImplementation()
    
    @staticmethod
    def display_all():
        products = RecepManagementLib.dao_service.display_all_products()
        for product in products:
            print(product)
            
    @staticmethod
    def add_patient():
        patient = Patient()
        
        #user input the product details
        first_name = input("Enter First name:")
        patient.first_name = first_name
        last_name = input("Enter Last name:")
        patient.last_name = last_name
        gender = input("Enter Gender:")
        patient.gender = gender
        DOB = input("Enter Date of birth(DD/MM/YYYY):")
        #convert string to object
        date_object = datetime.strptime(DOB,"%d/%m/%Y")
        #convert to mysql format YYYY-MM-DD
        msql_date = date_object.strftime("%Y-%m-%d") 
        patient.DOB = msql_date
        age = input("Enter age:")
        patient.age = age
        phone = input("Enter Phone number:")
        patient.phone = phone
        address = input("Enter Address:")
        patient.address = address
        email = input("Enter email:")
        patient.email = email
        created_on = input("Enter Created Date:")
        #convert string to object
        date_object = datetime.strptime(created_on,"%d/%m/%Y")
        #convert to mysql format YYYY-MM-DD
        msql_date = date_object.strftime("%Y-%m-%d")
        patient.created_on = msql_date
        
        if RecepManagementLib.dao_service.insert_patient(patient):
            print("inserted successfully....")
            
        else:
            print("something went wrong") 
    
    @staticmethod        
    def search_by_id():
        id = int(input("Enter id:"))
        products = RecepManagementLib.dao_service.searchby_id(id)
        for product in products:
            print(product)
            
    @staticmethod
    def update_product():
        searchid = int(input("enter product id to be updated:")) 
        products:Patient = RecepManagementLib.dao_service.searchby_id(searchid)
        products = products[0] 
        if not products:
            print("product not found!!")
            return
        confirm = input("Do you want to edit details?(Y/N)")
        if confirm.lower()=='y':
            products.unitprice = float(input("enter new unit price:")) 
            #pass the updated object to Dao for updating
            if RecepManagementLib.dao_service.update_product(products,searchid):
                print("updated successfully")
            else:
                print("something went wrong")