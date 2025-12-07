from datetime import date

class Appointment:
    """Appointment class  OOP applied here"""

    def __init__(self, appointment_id=None, appointment_date=None, appointment_time=None,
                 token_no=None, status=None, patient_id=None, doctor_id=None):

        self.__appointment_id = appointment_id
        self.__appointment_date = appointment_date
        self.__appointment_time = appointment_time
        self.__token_no = token_no
        self.__status = status
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id

    @property
    def appointment_id(self):
        return self.__appointment_id

    @property
    def appointment_date(self):
        return self.__appointment_date

    @property
    def appointment_time(self):
        return self.__appointment_time

    @property
    def token_no(self):
        return self.__token_no

    @property
    def status(self):
        return self.__status

    @property
    def patient_id(self):
        return self.__patient_id

    @property
    def doctor_id(self):
        return self.__doctor_id

    @appointment_id.setter
    def appointment_id(self, value):
        self.__appointment_id = value

    @appointment_date.setter
    def appointment_date(self, value):
        self.__appointment_date = value

    @appointment_time.setter
    def appointment_time(self, value):
        self.__appointment_time = value

    @token_no.setter
    def token_no(self, value):
        self.__token_no = value

    @status.setter
    def status(self, value):
        self.__status = value

    @patient_id.setter
    def patient_id(self, value):
        self.__patient_id = value

    @doctor_id.setter
    def doctor_id(self, value):
        self.__doctor_id = value

    def __str__(self):
        return (
            f"Appointment ID: {self.__appointment_id}, "
            f"Appointment Date: {self.__appointment_date}, "
            f"Appointment Time: {self.__appointment_time}, "
            f"Token No: {self.__token_no}, "
            f"Status: {self.__status}, "
            f"Patient ID: {self.__patient_id}, "
            f"Doctor ID: {self.__doctor_id}"
        )
