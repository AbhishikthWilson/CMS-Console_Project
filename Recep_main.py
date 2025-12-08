#from Lib.RecepMangementlib import RecepManagementLib

def recep_dashboard():
    while True:
        print("*" * 80)
        print("\t\tWelcome To Patient Management")
        print('''
               1. Add Patient
               2. Update Patient
               3. Search BY Patient ID
               4. Add appointment
               5. Payment and Billing
               6. View appointment
               7. Logout
               ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            #RecepManagementLib.add_patient()
            pass

        elif choice == '2':
            #RecepManagementLib.update_product()
            pass
        elif choice == '3':
            #RecepManagementLib.search_by_id()
            pass
        elif choice == '4':
           # RecepManagementLib.add_appointment()
           pass
        elif choice == '5':
            #RecepManagementLib.billing()
            pass
        elif choice == '6':
            #RecepManagementLib.view_appointment()
            pass
        elif choice == '7':
            print("Logging out...")
            break
        
        else:
            print("Invalid choice, try again.")
