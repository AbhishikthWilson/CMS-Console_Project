from datetime import date

class Roles:
    """Roles class OOP applied"""

    def __init__(self, role_id=None, role_name=None):

        self.__role_id = role_id
        self.__role_name = role_name


    @property
    def role_id(self):
        return self.__role_id

    @property
    def role_name(self):
        return self.__role_name


    @role_id.setter
    def role_id(self, value):
        self.__role_id = value

    @role_name.setter
    def role_name(self, value):
        self.__role_name = value


    def __str__(self):
        return (
            f"Role ID: {self.__role_id}, "
            f"Role Name: {self.__role_name}, "
        )
