from datetime import date

class Doctor:
    """Doctor class OOP applied"""

    def __init__(self, doctor_id=None, specialization=None, doctor_fee=None,
                 working_time=None, staff_id=None):

        self.__doctor_id = doctor_id
        self.__specialization = specialization
        self.__doctor_fee = doctor_fee
        self.__working_time = working_time
        self.__staff_id = staff_id


    @property
    def doctor_id(self):
        return self.__doctor_id

    @property
    def specialization(self):
        return self.__specialization

    @property
    def doctor_fee(self):
        return self.__doctor_fee

    @property
    def working_time(self):
        return self.__working_time

    @property
    def staff_id(self):
        return self.__staff_id


    @doctor_id.setter
    def doctor_id(self, value):
        self.__doctor_id = value

    @specialization.setter
    def specialization(self, value):
        self.__specialization = value

    @doctor_fee.setter
    def doctor_fee(self, value):
        self.__doctor_fee = value

    @working_time.setter
    def working_time(self, value):
        self.__working_time = value

    @staff_id.setter
    def staff_id(self, value):
        self.__staff_id = value


    def __str__(self):
        return (
            f"Doctor ID: {self.__doctor_id}, "
            f"Specialization: {self.__specialization}, "
            f"Doctor Fee: {self.__doctor_fee}, "
            f"Working Time: {self.__working_time}, "
            f"Staff ID: {self.__staff_id}"
        )
