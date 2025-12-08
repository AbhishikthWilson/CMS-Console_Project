from abc import abstractmethod,ABC
from Models.Patient import Patient


class PatientDaoService(ABC):
    
    # @abstractmethod
    # def patient_display_all(self):
    #     """fetch all patients details"""
    #     pass
    
    @abstractmethod
    def add_patient(self):
        """Add patient details"""
        pass
    
    @abstractmethod
    def update_patient(self,patient:Patient,patient_id:int,field_name:str):
        """Update patient by id"""
        pass
    
    @abstractmethod
    def search_by_patient_id(self,value):
        """search by patient id"""
        pass
    
    # @abstractmethod
    # def add_appointment(self):
    #     """add appointment"""
    #     pass
    
    # @abstractmethod
    # def payment_and_billing(self):
    #     """payment and billing"""
    #     pass
    
    # @abstractmethod
    # def view_appointment(self):
    #     """view appointment"""
    #     pass