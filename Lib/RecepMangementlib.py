from datetime import datetime
from Dao.RecepAbstract import PatientDaoService
from Dao.recepdaoimplement import RecepDaoImplementation
from Models.Patient import Patient

class RecepManagementLib:   
    """handles CRUD logic"""
    
    dao_service : PatientDaoService = RecepDaoImplementation()
    
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
        created_on = input("Enter Created Date(DD/MM/YYYY):")
        #convert string to object
        date_object = datetime.strptime(created_on,"%d/%m/%Y")
        #convert to mysql format YYYY-MM-DD
        msql_date = date_object.strftime("%Y-%m-%d")
        patient.created_on = msql_date
        
        if RecepManagementLib.dao_service.add_patient(patient):
            print("inserted successfully....") 
            
        else:
            print("something went wrong") 
    
    @staticmethod        
    def search_by_id():
        id = int(input("Enter id:"))
        patient = RecepManagementLib.dao_service.search_by_patient_id(id)
        print(patient)
            
    @staticmethod
    def update_patient():
        searchid = int(input("enter product id to be updated:")) 
        patient:Patient = RecepManagementLib.dao_service.search_by_patient_id(searchid) 
        if not patient:
            print("product not found!!")
            return
        confirm = input("Do you want to edit details?(Y/N)")
        if confirm.lower()=='y':
            print('''Choose which field to update 
                  1.first_name
                  2.gender
                  3.DOB
                  4.age
                  5.phone
                  6.address 
                  7.email
                  8.created_on 
                  ''')
            choice = input("enter choice:")
            if choice == '1': 
                field = "first_name"
                patient.first_name = input("Enter first_name:")
            elif choice == '2':
                field = "gender"
                patient.gender = input("enter gender:") 
            elif choice == '3':
                field = "DOB"
                patient.DOB = input("enter date of birth:")
                DOB = input("Enter Date of birth(DD/MM/YYYY):")
                #convert string to object
                date_object = datetime.strptime(DOB,"%d/%m/%Y")
                #convert to mysql format YYYY-MM-DD
                msql_date = date_object.strftime("%Y-%m-%d") 
                patient.DOB = msql_date
            elif choice == '4':
                field = "age"
                patient.age = input("enter age:") 
            elif choice =='5':
                field = "phone"
                patient.phone = input("enter phone:")
            elif choice =='6':
                field = "address"
                patient.address = input("enter address:")
            elif choice == '7':
                field = "email"
                patient.email = input("enter email:")  
            elif choice == '8':
                field = "created_on"
                created_on = input("enter created on(DD/MM/YYYY):")
                #convert string to object
                date_object = datetime.strptime(created_on,"%d/%m/%Y")
                #convert to mysql format YYYY-MM-DD
                msql_date = date_object.strftime("%Y-%m-%d")
                patient.created_on = msql_date      
            else:
                print("invalid")                          
                   
            #pass the updated object to Dao for updating
            if RecepManagementLib.dao_service.update_patient(patient,searchid,field):
                print("updated successfully")
            else:
                print("something went wrong")