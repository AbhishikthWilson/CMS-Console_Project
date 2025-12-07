from datetime import date

class StoreCredentials:
    """StoreCredentials class OOP applied here"""

    def __init__(self, cred_id=None, username=None, password=None,
                 role_id=None):

        self.__cred_id = cred_id
        self.__username = username
        self.__password = password
        self.__role_id = role_id

    @property
    def cred_id(self):
        return self.__cred_id

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def role_id(self):
        return self.__role_id


    @cred_id.setter
    def cred_id(self, value):
        self.__cred_id = value

    @username.setter
    def username(self, value):
        self.__username = value

    @password.setter
    def password(self, value):
        self.__password = value

    @role_id.setter
    def role_id(self, value):
        self.__role_id = value

    def __str__(self):
        return (
            f"Credential ID: {self.__cred_id}, "
            f"Username: {self.__username}, "
            f"Password: {self.__password}, "
            f"Role ID: {self.role_id}, "
        )
