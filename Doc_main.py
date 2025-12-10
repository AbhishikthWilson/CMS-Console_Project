from Lib.doctorlib import DoctorManagementLib

def doctor_dashboard():
    while True:
        print("""
    ================ Doctor Dashboard ================
    1. View Appointments
    2. View Patients
    3. Add Prescription
    4. Logout
    """)
        choice = input("Enter your choice: ")
        if choice == "1":
            DoctorManagementLib.view_appointment()

        elif choice == "2":
            DoctorManagementLib.view_patient()

        elif choice == "3":
            DoctorManagementLib.add_prescription()

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid choice. Try again.")
