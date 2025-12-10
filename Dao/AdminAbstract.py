from abc import ABC, abstractmethod


class AdminDaoServies(ABC):

    @abstractmethod
    def add_staff(self, staff):
        pass

    @abstractmethod
    def update_staff(self, staff, staff_id):
        pass

    @abstractmethod
    def view_staff(self):
        pass

    @abstractmethod
    def find_by_id(self, staff_id):
        pass

    @abstractmethod
    def delete_staff(self, staff_id):
        pass
