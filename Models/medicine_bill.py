from datetime import date

class MedicineBill:
    """Billing class OOP applied"""

    def __init__(self, bill_id=None,item_id=None , total_amount=None, bill_date=None):

        self.__bill_id = bill_id
        self.__item_id = item_id
        self.__total_amount = total_amount
        self.__bill_date = bill_date


    @property
    def bill_id(self):
        return self.__bill_id
    
    @property
    def item_id(self):
        return self.__item_id

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def bill_date(self):
        return self.__bill_date


    @bill_id.setter
    def bill_id(self, value):
        self.__bill_id = value

    @item_id.setter
    def item_id(self, value):
        self.__item_id = value    

    @total_amount.setter
    def total_amount(self, value):
        self.__total_amount = value

    @bill_date.setter
    def bill_date(self, value):
        self.__bill_date = value



    def __str__(self):
        return (
            f"Bill ID: {self.__bill_id}, "
            f"Item ID: {self.__item_id}"
            f"Total Amount: {self.__total_amount}, "
            f"Bill Date: {self.__bill_date}, "
        )
