from Dao.AbstractMedicineDao import MedicineDaoService
from Dao.MedicineDaoImple import MedicineDaoImplementation
from Dao.PrescriptionDaoImple import PrescriptionDaoImplementation
from Dao.BillDaoImple import BillDaoImplementation
from Models.medicine import Medicine
from datetime import datetime
from Validation.pharaValidatation import (
    validate_medicine_name,
    validate_category,
    validate_company_name,
    validate_quantity,
    validate_price,
    validate_expiry_date
)


class MedicineManagementLib:
    """Handles CRUD logic"""

    dao_service: MedicineDaoService = MedicineDaoImplementation()
    prescription_dao = PrescriptionDaoImplementation()
    bill_dao = BillDaoImplementation()

    # ============ USE CASE 1: ADD NEW MEDICINE ============
    @staticmethod
    def insert_medicines():
        med = Medicine()

        # Medicine Name
        while True:
            try:
                med.medicine_name = validate_medicine_name(input("Enter the medicine name: "))
                break
            except Exception as e:
                print("Validation Error:", e)

        # Category
        while True:
            try:
                med.category = validate_category(input("Enter the category: "))
                break
            except Exception as e:
                print("Validation Error:", e)

        # Company Name
        while True:
            try:
                med.company_name = validate_company_name(input("Enter the company name: "))
                break
            except Exception as e:
                print("Validation Error:", e)

        # Quantity
        while True:
            try:
                med.quantity = validate_quantity(input("Enter the quantity: "))
                break
            except Exception as e:
                print("Validation Error:", e)

        # Price
        while True:
            try:
                med.price = validate_price(input("Enter the unit price: "))
                break
            except Exception as e:
                print("Validation Error:", e)

        # Expiry Date
        while True:
            try:
                med.expiry_date = validate_expiry_date(input("Enter expiry date (DD/MM/YYYY): "))
                break
            except Exception as e:
                print("Validation Error:", e)

        # Insert to DB
        if MedicineManagementLib.dao_service.insert_medicines(med):
            print("Medicine inserted successfully!")
        else:
            print("Something went wrong!")

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
