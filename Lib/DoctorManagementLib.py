from Models.doctor import Doctor
from Dao.DoctorDaoImplementation import DoctorDaoImplementation

class DoctorManagementLib:

    dao = DoctorDaoImplementation()

    @staticmethod
    def doctor_menu():
        while True:
            print("\nDoctor Management:")
            print("1. Add Doctor")
            print("2. View Doctors")
            print("3. Update Doctor")
            print("4. Activate/Inactivate Doctor")
            print("5. Back")

            choice = input("Enter choice: ")

            if choice == '1':
                DoctorManagementLib.add_doctor()
            elif choice == '2':
                DoctorManagementLib.view_doctors()
            elif choice == '3':
                DoctorManagementLib.update_doctor()
            elif choice == '4':
                DoctorManagementLib.delete_doctor()
            elif choice == '5':
                break
            else:
                print("Invalid choice")

    @staticmethod
    def add_doctor():
        d = Doctor()
        d.specialization = input("Enter specialization: ")
        d.doctor_fee = input("Enter fee: ")
        d.working_time = input("Enter working time: ")
        d.staff_id = input("Enter staff ID: ")

        if DoctorManagementLib.dao.add_doctor(d):
            print("Doctor added successfully")
        else:
            print("Error adding doctor")

    @staticmethod
    def view_doctors():
        docs = DoctorManagementLib.dao.view_doctors()
        if not docs:
            print("No doctors found.")
        else:
            for d in docs:
                print(d)

    @staticmethod
    def update_doctor():
        doctor_id = int(input("Enter doctor ID to update: "))

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
            d.specialization = input("Enter new specialization: ")
        elif choice == '2':
            d.doctor_fee = input("Enter new fee: ")
        elif choice == '3':
            d.working_time = input("Enter new working time: ")
        elif choice == '4':
            d.staff_id = input("Enter new staff ID: ")
        else:
            print("Invalid option")
            return

        if DoctorManagementLib.dao.update_doctor(d, doctor_id):
            print("Updated successfully")
        else:
            print("Failed to update")

    @staticmethod
    def delete_doctor():
        doctor_id = int(input("Enter doctor ID to delete: "))
        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() != 'y':
            print("Cancelled.")
            return

        if DoctorManagementLib.dao.delete_doctor(doctor_id):
            print("Doctor deleted successfully")
        else:
            print("Error deleting doctor")
