from datetime import date

class Token:
    """Roles class OOP applied"""

    def __init__(self, token_no=None, token_id=None):

        self.__token_no = token_no
        self.__token_id = token_id


    @property
    def token_no(self):
        return self.__token_no

    @property
    def token_id(self):
        return self.__token_id


    @token_no.setter
    def token_no(self, value):
        self.__token_no = value

    @token_id.setter
    def token_id(self, value):
        self.__token_id = value


    def __str__(self):
        return (
            f"Token No: {self.__token_no}, "
            f"Token ID: {self.__token_id}, "
        )
