from Lib.AdminManagementLib import AdminManagementLib
from Lib.DoctorManagementLib import DoctorManagementLib


def admin_dashboard():
    while True:
        print('''\nAdmin Dashboard:
              
                1. Manage Staff
                2. Manage Doctor
                3. Logout
              ''')
        choice = input("Enter your choice: ")

        if choice == '1':
            AdminManagementLib.staff_menu()

        elif choice == '2':
            DoctorManagementLib.doctor_menu()

        elif choice == '3':
            print("Logging out...")
            break

        else:
            print("Invalid choice. Try again.")
