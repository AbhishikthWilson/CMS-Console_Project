from Lib.RecepMangementlib import RecepManagementLib

def recep_dashboard():
    while True:
        print("*" * 80)
        print("\t\tWelcome To Patient Management")
        print('''
               1. Add Patient
               2. Update Patient
               3. Search BY Patient ID
               4. View Patient List
               5. Add appointment
               6. Payment and Billing
               7. View appointment
               8. Logout
               ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            RecepManagementLib.add_patient()

        elif choice == '2':
            RecepManagementLib.update_patient()

        elif choice == '3':
            RecepManagementLib.search_by_id()

        elif choice == '4':
            RecepManagementLib.display_all()   
            
        elif choice == '5':
            RecepManagementLib.add_appointment()
            
        elif choice == '6':
            RecepManagementLib.payment_and_billing()
            
        elif choice == '7':
            RecepManagementLib.view_appointment()
            
        elif choice == '8':
            print("Logging out...")
            break
        
        else:
            print("Invalid choice, try again.")
