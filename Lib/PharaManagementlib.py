from Dao.AbstractMedicineDao import MedicineDaoService
from Dao.MedicineDaoImple import MedicineDaoImplementation

from Dao.PrescriptionDaoImple import PrescriptionDaoImplementation
from Dao.BillDaoImple import BillDaoImplementation
from Models.medicine import Medicine
# from Models.medicine_bill import MedicineBill
from datetime import datetime 

class  MedicineManagementLib:
    '''handles CRUD logic'''
    dao_service:MedicineDaoService=MedicineDaoImplementation()
    prescription_dao = PrescriptionDaoImplementation()
    # dao_service = MedicineDaoImplementation()
    bill_dao = BillDaoImplementation()
    # dao_service = MedicineDaoImplementation()


    @staticmethod
    def insert_medicines():
        med=Medicine()
        med_name=input("Enter the medicine name:")
        med.medicine_name=med_name 
        med_category=input("Enter the category:")
        med.category=med_category
        med_company_name=input("Enter the company name: ")
        med.company_name=med_company_name
        med_quantity=int(input("Enter the quantity: "))
        med.quantity=med_quantity
        med_price=float(input("Enter the unit price:"))
        med.price=med_price
        #user input date->database date format
        med_expiry_date=input("Enter the expiry date(DD/MM/YYYY):")
        #convert string to date object
        date_object=datetime.strptime(med_expiry_date,"%d/%m/%Y")
        #convert to mysql.format YYYY-MM-DD
        mysql_date=date_object.strftime("%Y-%m-%d")
        med.expiry_date=mysql_date

        if  MedicineManagementLib.dao_service.insert_medicines(med):
            print("Medicine inserted successfully!")
        else:
            print("something went wrong!!!")

    @staticmethod
    def display_all_medicines():
        print("\n--- LIST OF MEDICINES ---")
        medicines=MedicineManagementLib.dao_service.display_all_medicines()
        if not medicines:
            print("No medicines found.")
            return
        for med in medicines:
            print(med)

    # ============ USE CASE 2: VIEW LIST OF MEDICINES ============
    @staticmethod
    def display_all_medicines():
        print("\n--- LIST OF MEDICINES ---")
        medicines = MedicineManagementLib.dao_service.display_all_medicines()
        if not medicines:
            print("No medicines found.")
            return

        for med in medicines:
            print(med)

    # ============ USE CASE 3: SEARCH MEDICINES ============
    @staticmethod
    def search_medicines_by_name():
        print("\n--- SEARCH MEDICINES ---")
        name = input("Enter medicine name to search: ").strip()
        if not name:
            print("Please enter a search value.")
            return

        medicines = MedicineManagementLib.dao_service.search_medicines_by_name(name)
        if not medicines:
            print("No Data Found.")
        else:
            for med in medicines:
                print(med)
    
    # ============ USE CASE 4: DISPENSE MEDICINE ============
    @staticmethod
    def dispense_medicine():
        print("\n--- DISPENSE MEDICINE (BASED ON PRESCRIPTION) ---")
        try:
            presc_id = int(input("Enter Prescription ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        presc = MedicineManagementLib.prescription_dao.get_prescription_by_id(presc_id)
        if not presc:
            print("Prescription not found.")
            return

        med = MedicineManagementLib.dao_service.find_by_medicine_id(presc["medicine_id"])
        if not med:
            print("Medicine not found in stock.")
            return

        print("\nPrescription Details:")
        print(f"Prescription ID : {presc['prescription_id']}")
        print(f"Medicine  Name  : {med.medicine_name}")
        print(f"Medicine ID     : {med.medicine_id}")
        print(f"Dosage          : {presc['dosage']}")
        print(f"Frequency       : {presc['frequency']}")
        print(f"Duration        : {presc['duration']}")
        print(f"Quantity needed : {presc['quantity']}")
        print(f"Stock available : {med.quantity}")

        if med.quantity < presc["quantity"]:
            print("Not enough stock to dispense this prescription.")
            return

        confirm = input("\nDispense this medicine? (Y/N): ").strip().lower()
        if confirm != "y":
            print("Dispense cancelled.")
            return

        new_qty = med.quantity - presc["quantity"]
        if MedicineManagementLib.dao_service.update_medicine_quantity(med.medicine_id, new_qty):
            print("Medicine dispensed. Stock updated.")
        else:
            print("Failed to update stock.")

    # ============ USE CASE 5: GENERATE BILL ============
    @staticmethod
    def generate_patient_bill():
        print("\n--- GENERATE BILL FROM PRESCRIPTION ---")
        try:
            presc_id = int(input("Enter Prescription ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        presc = MedicineManagementLib.prescription_dao.get_prescription_by_id(presc_id)
        if not presc:
            print("Prescription not found.")
            return

        med = MedicineManagementLib.dao_service.find_by_medicine_id(presc["medicine_id"])
        if not med:
            print("Medicine not found.")
            return

        qty = presc["quantity"]
        total_amount = qty * med.price

        print("\nBill Preview:")
        print(f"Prescription ID : {presc['prescription_id']}")
        print(f"Medicine        : {med.medicine_name}")
        print(f"Quantity        : {qty}")
        print(f"Unit price      : {med.price}")
        print(f"Total amount    : {total_amount}")

        confirm = input("\nConfirm bill generation? (Y/N): ").strip().lower()
        if confirm != "y":
            print("Bill cancelled.")
            return

        if MedicineManagementLib.bill_dao.create_bill_for_prescription(presc_id, total_amount):
            print("Bill generated and stored successfully.")
            print(f"Total Amount: {total_amount}")
        else:
            print("Error while generating bill.")

    # ============ USE CASE 6: VIEW BILL HISTORY ============
    @staticmethod
    def view_bill_history():
        print("\n--- BILL HISTORY ---")
        bills = MedicineManagementLib.bill_dao.get_all_bills()
        if not bills:
            print("No bills found.")
            return

        for b in bills:
            print(
                f"Bill ID: {b['bill_id']}, "
                f"Date: {b['bill_date']}, "
                f"Total: {b['total_amount']}, "
                f"Medicine: {b['medicine_name']}, "
                f"Qty: {b['quantity']}"
            )

        detail_choice = input("\nView details of any bill? (Y/N): ").strip().lower()
        if detail_choice != 'y':
            return

        try:
            bill_id = int(input("Enter Bill ID: "))
        except ValueError:
            print("Invalid Bill ID.")
            return

        d = MedicineManagementLib.bill_dao.get_bill_details(bill_id)
        if not d:
            print("Bill not found.")
            return

        print("\n--- BILL DETAILS ---")
        print(f"Bill ID        : {d['bill_id']}")
        print(f"Bill Date      : {d['bill_date']}")
        print(f"Total Amount   : {d['total_amount']}")
        print(f"Item ID        : {d['item_id']}")
        print(f"Prescription ID: {d['prescription_id']}")
        print(f"Medicine ID    : {d['medicine_id']}")
        print(f"Medicine Name  : {d['medicine_name']}")
        print(f"Dosage         : {d['dosage']}")
        print(f"Frequency      : {d['frequency']}")
        print(f"Duration       : {d['duration']}")
        print(f"Quantity       : {d['quantity']}")
        print(f"Unit Price     : {d['price']}")
 

