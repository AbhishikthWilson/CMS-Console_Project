from datetime import date

class ReceptionistBilling:
    """Billing class OOP applied"""

    def __init__(self, bill_id=None, total_amount=None, bill_date=None,
                 appointment_id=None, staff_id=None):

        self.__bill_id = bill_id
        self.__total_amount = total_amount
        self.__bill_date = bill_date
        self.__appointment_id = appointment_id
        self.__staff_id = staff_id


    @property
    def bill_id(self):
        return self.__bill_id

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def bill_date(self):
        return self.__bill_date

    @property
    def appointment_id(self):
        return self.__appointment_id

    @property
    def staff_id(self):
        return self.__staff_id


    @bill_id.setter
    def bill_id(self, value):
        self.__bill_id = value

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value

    @bill_date.setter
    def bill_date(self, value):
        self.__bill_date = value

    @appointment_id.setter
    def appointment_id(self, value):
        self.__appointment_id = value

    @staff_id.setter
    def staff_id(self, value):
        self.__staff_id = value


    def __str__(self):
        return (
            f"Bill ID: {self.__bill_id}, "
            f"Total Amount: {self.__total_amount}, "
            f"Bill Date: {self.__bill_date}, "
            f"Appointment ID: {self.__appointment_id}, "
            f"Staff ID: {self.__staff_id}"
        )
