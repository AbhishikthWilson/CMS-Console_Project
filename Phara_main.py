def pharmacist_dashboard():
    while True:
        print("*" * 80)
        print("\t\tWELCOME TO PHARMACIST MEDICINE MANAGEMENT")
        print('''
1. ADD NEW MEDICINE
2. VIEW LIST OF MEDICINES
3. SEARCH MEDICINES BY NAME
4. DISPENSE MEDICINE (BASED ON PRESCRIPTION)
5. GENERATE PATIENT BILL
6. VIEW BILLS (BILL HISTORY)
7. Logout
''')

        choice = input("Enter your choice: ")

        if choice == "1":
            # MedicineManagementLib.add_medicine()
            pass

        elif choice == "2":
            # MedicineManagementLib.display_all_medicines()
            pass
        elif choice == "3":
            # MedicineManagementLib.search_medicines()
            pass
        elif choice == "4":
            # MedicineManagementLib.dispense_medicine()
            pass
        elif choice == "5":
            # MedicineManagementLib.generate_patient_bill()
            pass
        elif choice == "6":
            # MedicineManagementLib.view_bill_history()
            pass
        elif choice == "7":
            print("Logging out...")
            break

        else:
            print("Invalid choice! Please try again.")
