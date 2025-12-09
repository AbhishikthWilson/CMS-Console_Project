from datetime import datetime
from Dao.RecepAbstract import PatientDaoService
from Dao.recepdaoimplement import RecepDaoImplementation
from Models.patient import Patient
from Models.appointment import Appointment
from Models.doctor import Doctor
from Models.receptionist_billing import ReceptionistBilling
from Models.staff import Staff

class RecepManagementLib:   
    """handles CRUD logic"""
    
    dao_service : PatientDaoService = RecepDaoImplementation()
    
    @staticmethod
    def display_all():
        patients = RecepManagementLib.dao_service.patient_display_all()
        for patient in patients:
            print(patient)
            
    @staticmethod
    def add_patient():
        print("\n--- Add Patient ---")

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
        print("\n--- Search Patient ---")

        id = int(input("Enter id:"))
        patient = RecepManagementLib.dao_service.search_by_patient_id(id)
        print(patient)
            
    @staticmethod
    def update_patient():
        print("\n--- Update Patient ---")

        searchid = int(input("enter patient id to be updated:"))  
        patient:Patient = RecepManagementLib.dao_service.search_by_patient_id(searchid) 
        if not patient:
            print("patient not found!!")
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
    
    @staticmethod
    def add_appointment():
        appointment = Appointment()

        print("\n--- Add Appointment ---")
        
        appointment_date = input("Enter Appointment Date (DD/MM/YYYY): ")
        #convert string to object
        date_object = datetime.strptime(appointment_date,"%d/%m/%Y")
        #convert to mysql format YYYY-MM-DD
        msql_date = date_object.strftime("%Y-%m-%d")
        appointment.appointment_date = msql_date

        appointment_time = input("Enter Appointment Time (HH:MM): ")
        time_object = datetime.strptime(appointment_time, "%H:%M")
        mysql_time = time_object.strftime("%H:%M:%S")
        appointment.appointment_time = mysql_time

        token_no = int(input("Enter Token Number: "))
        appointment.token_no = token_no
        status = input("Enter Status (Pending/Confirmed): ") 
        appointment.status = status

        patient_id = int(input("Enter Patient ID: "))
        patient:Patient = RecepManagementLib.dao_service.search_by_patient_id(patient_id) 
        if not patient:
            print("patient not found!!")
            return
        appointment.patient_id = patient_id

        doctor_id = int(input("Enter Doctor ID: "))  
        doctor:Doctor = RecepManagementLib.dao_service.search_by_doctor_id(doctor_id) 
        if not doctor:
            print("doctor not found!!")
            return
        appointment.doctor_id = doctor_id 

        if RecepManagementLib.dao_service.add_appointment(appointment):
                print("Added successfully")
        else:
                print("something went wrong")
    
    @staticmethod
    def view_appointment():
        appointments = RecepManagementLib.dao_service.view_appointment()
        for appointment in appointments:
            print(appointment) 
    
    @staticmethod
    def payment_and_billing():
        billing = ReceptionistBilling()

        print("\n--- Payment and Billing ---")
        
        total_amount = int(input("Enter Amount: "))
        billing.total_amount = total_amount

        bill_date = input("Enter Payment Date (DD/MM/YYYY): ")
        #convert string to object
        date_object = datetime.strptime(bill_date,"%d/%m/%Y")
        #convert to mysql format YYYY-MM-DD
        msql_date = date_object.strftime("%Y-%m-%d")
        billing.bill_date = msql_date

        appointment_id = int(input("Enter Appointment ID: "))
        appointment:Appointment = RecepManagementLib.dao_service.search_by_appointment_id(appointment_id) 
        if not appointment:
            print("appointment not found!!")
            return
        billing.appointment_id = appointment_id

        staff_id = int(input("Enter Staff ID: "))  
        staff:Staff = RecepManagementLib.dao_service.search_by_staff_id(staff_id) 
        if not staff:
            print("staff not found!!")
            return
        billing.staff_id = staff_id 

        if RecepManagementLib.dao_service.payment_and_billing(billing):
                print("Added successfully")
        else:
                print("something went wrong") 
    
    @staticmethod
    def view_bill():                                      
        bills = RecepManagementLib.dao_service.view_bill()
        for bill in bills:
            print(bill) 