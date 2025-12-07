from datetime import date

class PrescriptionItem:
    """PrescriptionItem class OOP applied"""

    def __init__(self, item_id=None, prescription_id=None):

        self.__item_id = item_id
        self.__prescription_id = prescription_id


    @property
    def item_id(self):
        return self.__item_id

    @property
    def prescription_id(self):
        return self.__prescription_id


    @item_id.setter
    def item_id(self, value):
        self.__item_id = value

    @prescription_id.setter
    def prescription_id(self, value):
        self.__prescription_id = value


    def __str__(self):
        return (
            f"Item ID: {self.__item_id}, "
            f"Prescription ID: {self.__prescription_id}, "
        )
