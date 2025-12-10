from Models.doctor import Doctor
from Dao.DoctorDaoImplementation import DoctorDaoImplementation
from Validation.RecepValidate import validate_name, validate_phone, validate_email, validate_role_id

class DoctorManagementLib:

    dao = DoctorDaoImplementation()

    @staticmethod
    def doctor_menu():
        while True:
            print("\nDoctor Management:")
            print("1. Add Doctor")
            print("2. View Doctors")
            print("3. Update Doctor")
            print("4. Back")

            choice = input("Enter choice: ")

            if choice == '1':
                DoctorManagementLib.add_doctor()
            elif choice == '2':
                DoctorManagementLib.view_doctors()
            elif choice == '3':
                DoctorManagementLib.update_doctor()
            elif choice == '4':
                break
            else:
                print("Invalid choice")


    # ------------------- ADD DOCTOR -------------------
    @staticmethod
    def add_doctor():
        d = Doctor()

        # Specialization
        while True:
            spec = input("Enter specialization: ")
            if len(spec) >= 2:
                d.specialization = spec
                break
            print("Specialization must be at least 2 characters")

        # Fee
        while True:
            fee = input("Enter doctor fee: ")
            if fee.isdigit():
                d.doctor_fee = int(fee)
                break
            print("Doctor fee must be a number")

        # Working time
        while True:
            wt = input("Enter working time (e.g., 10AM-4PM): ")
            if len(wt) >= 4:
                d.working_time = wt
                break
            print("Working time must be valid text")

        # Staff ID
        while True:
            sid = input("Enter staff ID: ")
            if sid.isdigit():
                d.staff_id = int(sid)
                break
            print("Staff ID must be a numeric value")

        # Insert into DB
        if DoctorManagementLib.dao.add_doctor(d):
            print("Doctor added successfully")
        else:
            print("Error adding doctor")


    # ------------------- VIEW DOCTORS -------------------
    @staticmethod
    def view_doctors():
        docs = DoctorManagementLib.dao.view_doctors()
        if not docs:
            print("No doctors found.")
        else:
            for d in docs:
                print(d)


    # ------------------- UPDATE DOCTOR -------------------
    @staticmethod
    def update_doctor():
        doctor_id = input("Enter doctor ID to update: ")

        if not doctor_id.isdigit():
            print("Invalid doctor ID")
            return
        doctor_id = int(doctor_id)

        d = DoctorManagementLib.dao.find_by_id(doctor_id)
        if not d:
            print("Doctor not found!")
            return

        print("\nWhat do you want to update?")
        print("1. Specialization")
        print("2. Fee")
        print("3. Working Time")
        print("4. Staff ID")

        choice = input("Enter choice: ")

        if choice == '1':
            new_spec = input("Enter new specialization: ")
            if len(new_spec) < 2:
                print("Invalid specialization")
                return
            d.specialization = new_spec

        elif choice == '2':
            fee = input("Enter new fee: ")
            if not fee.isdigit():
                print("Fee must be numeric")
                return
            d.doctor_fee = int(fee)

        elif choice == '3':
            wt = input("Enter new working time: ")
            if len(wt) < 4:
                print("Invalid working time")
                return
            d.working_time = wt

        elif choice == '4':
            sid = input("Enter new staff ID: ")
            if not sid.isdigit():
                print("Staff ID must be numeric")
                return
            d.staff_id = int(sid)

        else:
            print("Invalid option")
            return

        if DoctorManagementLib.dao.update_doctor(d, doctor_id):
            print("Updated successfully")
        else:
            print("Failed to update")


    # # ------------------- ACTIVATE/INACTIVATE DOCTOR -------------------
    # @staticmethod
    # def delete_doctor():
    #     doctor_id = input("Enter doctor ID to activate/inactivate: ")

    #     if not doctor_id.isdigit():
    #         print("Invalid doctor ID")
    #         return

    #     doctor_id = int(doctor_id)

    #     d = DoctorManagementLib.dao.find_by_id(doctor_id)

    #     if not d:
    #         print("Doctor not found!")
    #         return

    #     print(f"Current status: {d.status}")
    #     new_status = input("Enter new status (active/inactive): ").lower()

    #     if new_status not in ["active", "inactive"]:
    #         print("Invalid status")
    #         return

    #     d.status = new_status

    #     if DoctorManagementLib.dao.update_doctor(d, doctor_id):
    #         print(f"Doctor {new_status} successfully")
    #     else:
    #         print("Failed to update status")
