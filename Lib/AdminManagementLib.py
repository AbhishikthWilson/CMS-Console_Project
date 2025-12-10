from Models.staff import Staff
from Dao.AdminAbstract import AdminDaoServies
from Dao.AdminAbstractImplementation import AdminAbstractImplementation
from Validation.RecepValidate import validate_email, validate_name, validate_phone, validate_role_id


class AdminManagementLib:

    dao_service: AdminDaoServies = AdminAbstractImplementation()

        # ------------------------ STAFF MENU ------------------------
    @staticmethod
    def staff_menu():
        while True:
            print("\nStaff Management:")
            print("1. Add Staff")
            print("2. View Staff")
            print("3. Update Staff")
            print("4. Activate/Inactivate Staff")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == '1':
                AdminManagementLib.add_staff()
            elif choice == '2':
                AdminManagementLib.view_staff()
            elif choice == '3':
                AdminManagementLib.update_staff()
            elif choice == '4':
                AdminManagementLib.delete_staff()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Try again.")


    # ------------------------ INSERT ------------------------
    @staticmethod
    def add_staff():
        staff = Staff()

        # --- NAME ---
        while True:
            name = input("Enter staff name: ")
            try:
                validate_name(name)
                staff.name = name
                break
            except Exception as e:
                print(f"Staff name validation error: {e}")

        # --- EMAIL ---
        while True:
            email = input("Enter staff email: ")
            try:
                validate_email(email)
                staff.email = email
                break
            except Exception as e:
                print(f"Email validation error: {e}")

        # --- PHONE ---
        while True:
            phone = input("Enter phone number: ")
            try:
                validate_phone(phone)
                staff.phone = phone
                break
            except Exception as e:
                print(f"Phone validation error: {e}")

        # --- STATUS ---
        while True:
            st = input("Enter status (active/inactive): ").lower()
            if st in ["active", "inactive"]:
                staff.status = st
                break
            else:
                print("Invalid status. Please enter active/inactive")

        # --- CREATED DATE (no validation yet) ---
        staff.created_on = input("Enter created date (YYYY-MM-DD): ")

        # --- ROLE ID ---
        while True:
            rid = input("Enter role ID (1-Admin,2-Receptionist,3-Doctor,4-Pharmacist): ")
            try:
                rid = int(rid)
                validate_role_id(rid)
                staff.role_id = rid
                break
            except Exception as e:
                print(f"Role ID validation error: {e}")

        # --- INSERT into DB ---
        if AdminManagementLib.dao_service.add_staff(staff):
            print("Inserted Successfully")
        else:
            print("Something went wrong!")



    # ------------------------ VIEW ------------------------
    @staticmethod
    def view_staff():
        staffs = AdminManagementLib.dao_service.view_staff()

        if not staffs:
            print("No staff found.")
        else:
            for s in staffs:
                print(s)

    # ------------------------ UPDATE ------------------------
    @staticmethod
    def update_staff():
        staff_id = int(input("Enter Staff ID to update: "))

        staff = AdminManagementLib.dao_service.find_by_id(staff_id)

        if not staff:
            print("Staff not found!")
            return

        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Email")
        print("3. Phone")
        print("4. Status")
        print("5. Role ID")

        choice = input("Enter choice: ")

        try:
            if choice == '1':
                staff.name = input("Enter new name: ")
            elif choice == '2':
                staff.email = input("Enter new email: ")
            elif choice == '3':
                staff.phone = input("Enter new phone: ")
            elif choice == '4':
                new_status = input("Enter new status (active/inactive): ")
                if new_status.lower() not in ["active", "inactive"]:
                    print("Invalid status.")
                    return
                staff.status = new_status
            elif choice == '5':
                staff.role_id = int(input("Enter new role ID: "))
            else:
                print("Invalid option")
                return
        except Exception as e:
            print(f"Validation error: {e}")
            return

        if AdminManagementLib.dao_service.update_staff(staff, staff_id):
            print("Updated Successfully")
        else:
            print("Update Failed!")


        # ------------------------ DEACTIVATE STAFF (SOFT DELETE) ------------------------
    @staticmethod
    def delete_staff():
        staff_id = int(input("Enter Staff ID to deactivate: "))

        staff = AdminManagementLib.dao_service.find_by_id(staff_id)

        if not staff:
            print("Staff not found!")
            return

        confirm = input("Are you sure you want to deactivate this user? (y/n): ")

        if confirm.lower() != 'y':
            print("Cancelled.")
            return

        staff.status = "inactive"

        if AdminManagementLib.dao_service.update_staff(staff, staff_id):
            print("Staff deactivated successfully")
        else:
            print("Failed to deactivate staff")
