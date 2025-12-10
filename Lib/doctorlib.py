from datetime import datetime
from Dao.DoctorAbstract import DoctorAbstract
from Dao.DoctorAbstractlmplementation import DoctorDAOImpl
from Models.appointment import Appointment
from Models.patient import Patient


class DoctorManagementLib:
    """Handles Doctor Dashboard Operations"""

    dao_service: DoctorAbstract = DoctorDAOImpl()

    @staticmethod
    def view_appointment():
        appointment_id = int(input("Enter Appointment ID to search: "))
        appointment = DoctorManagementLib.dao_service.get_appointment_by_id(appointment_id)

        if appointment:
            print("\n--- Appointment Details ---")
            print(f"Appointment ID   : {appointment.appointment_id}")
            print(f"Date             : {appointment.appointment_date}")
            print(f"Time             : {appointment.appointment_time}")
            print(f"Token No         : {appointment.token_no}")
            print(f"Status           : {appointment.status}")
            print(f"Patient ID       : {appointment.patient_id}")
            print(f"Doctor ID        : {appointment.doctor_id}")
            print("---------------------------\n")
        else:
            print(f"No Appointment found with ID {appointment_id}")

    @staticmethod
    def view_patient():
        patient_id = int(input("Enter patient ID to search: "))
        patient = DoctorManagementLib.dao_service.get_patient_by_id(patient_id)

        if patient:
            print("\n--- Patient Details ---")
            print(f"Patient ID  : {patient.patient_id}")
            print(f"First Name  : {patient.first_name}")
            print(f"Last Name   : {patient.last_name}")
            print(f"Gender      : {patient.gender}")
            print(f"DOB         : {patient.DOB}")
            print(f"Age         : {patient.age}")
            print(f"Phone       : {patient.phone}")
            print(f"Address     : {patient.address}")
            print(f"Email       : {patient.email}")
            print(f"Created On  : {patient.created_on}")
            print("------------------------\n")
        else:
            print(f"No Patient found with ID {patient_id}")

    @staticmethod
    def add_prescription():
        appointment_id = int(input("Enter Appointment ID: "))
        medicine_id = int(input("Enter Medicine ID: "))
        dosage = input("Enter Dosage: ")
        frequency = input("Enter Frequency: ")
        duration = input("Enter Duration: ")
        quantity = int(input("Enter Quantity: "))

        if DoctorManagementLib.dao_service.add_prescription(
            appointment_id, medicine_id, dosage, frequency, duration, quantity
        ):
            print("Prescription Added Successfully")
        else:
            print("Failed to Add Prescription")
