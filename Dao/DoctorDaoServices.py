from abc import ABC, abstractmethod

class DoctorDaoServices(ABC):

    @abstractmethod
    def add_doctor(self, doctor):
        pass

    @abstractmethod
    def update_doctor(self, doctor, doctor_id):
        pass

    @abstractmethod
    def view_doctors(self):
        pass

    @abstractmethod
    def find_by_id(self, doctor_id):
        pass

    @abstractmethod
    def delete_doctor(self, doctor_id):
        pass
