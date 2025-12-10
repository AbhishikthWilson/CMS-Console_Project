from datetime import datetime
from Dao.DoctorAbstract import DoctorAbstract
from Dao.DoctorAbstractlmplementation import DoctorDAOImpl
from Models.appointment import Appointment
from Models.patient import Patient

# Import validation functions
from Validation.DoctorValidation import (
    validate_int,
    validate_non_empty,
    validate_dosage,
    validate_frequency,
    validate_duration
)


class DoctorManagementLib:
    """Handles Doctor Dashboard Operations"""

    dao_service: DoctorAbstract = DoctorDAOImpl()

    # ----------------- VIEW APPOINTMENT -----------------
    @staticmethod
    def view_appointment():
        appointment_id = validate_int("Enter Appointment ID to search: ", "Appointment ID")
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

    # ----------------- VIEW PATIENT -----------------
    @staticmethod
    def view_patient():
        patient_id = validate_int("Enter patient ID to search: ", "Patient ID")
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

    # ----------------- ADD PRESCRIPTION -----------------
    @staticmethod
    def add_prescription():
        appointment_id = validate_int("Enter Appointment ID: ", "Appointment ID")
        medicine_id = validate_int("Enter Medicine ID: ", "Medicine ID")
        dosage = validate_dosage()
        frequency = validate_frequency()
        duration = validate_duration()
        quantity = validate_int("Enter Quantity: ", "Quantity")

        success = DoctorManagementLib.dao_service.add_prescription(
            appointment_id, medicine_id, dosage, frequency, duration, quantity
        )

        if success:
            print("Prescription Added Successfully")
        else:
            print("Failed to Add Prescription")
