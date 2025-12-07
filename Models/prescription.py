from datetime import date

class Prescription:
    """Prescription class OOP applied here"""

    def __init__(self, prescription_id=None, dosage=None, frequency=None,
                 duration=None, quantity=None, appointment_id=None, medicine_id=None):

        self.__prescription_id = prescription_id
        self.__dosage = dosage
        self.__frequency = frequency
        self.__duration = duration
        self.__quantity = quantity
        self.__appointment_id = appointment_id
        self.__medicine_id = medicine_id

    @property
    def prescription_id(self):
        return self.__prescription_id

    @property
    def dosage(self):
        return self.__dosage

    @property
    def frequency(self):
        return self.__frequency

    @property
    def duration(self):
        return self.__duration

    @property
    def quantity(self):
        return self.__quantity

    @property
    def appointment_id(self):
        return self.__appointment_id

    @property
    def medicine_id(self):
        return self.__medicine_id

    @prescription_id.setter
    def prescription_id(self, value):
        self.__prescription_id = value

    @dosage.setter
    def dosage(self, value):
        self.__dosage = value

    @frequency.setter
    def frequency(self, value):
        self.__frequency = value

    @duration.setter
    def duration(self, value):
        self.__duration = value

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    @appointment_id.setter
    def appointment_id(self, value):
        self.__appointment_id = value

    @medicine_id.setter
    def medicine_id(self, value):
        self.__medicine_id = value

    def __str__(self):
        return (
            f"Prescription ID: {self.__prescription_id}, "
            f"Dosage: {self.__dosage}, "
            f"Frequency: {self.__frequency}, "
            f"Duration: {self.__duration}, "
            f"Quantity: {self.__quantity}, "
            f"Appointment ID: {self.__appointment_id}, "
            f"Medicine ID: {self.__medicine_id}"
        )
