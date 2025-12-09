from abc import abstractmethod,ABC
from Models.patient import Patient
from Models.appointment import Appointment
from Models.receptionist_billing import ReceptionistBilling


class PatientDaoService(ABC):
    
    @abstractmethod
    def patient_display_all(self):
        """fetch all patients details"""
        pass
    
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
    
    @abstractmethod
    def add_appointment(self, appointment: Appointment):
        pass
    
    @abstractmethod
    def payment_and_billing(self,billing:ReceptionistBilling):
        """payment and billing"""
        pass
    
    @abstractmethod
    def view_appointment(self):
        """view appointment"""
        pass

    @abstractmethod
    def search_by_doctor_id(self,value):
        """search by patient id"""
        pass

    @abstractmethod
    def search_by_appointment_id(self,value):
        """search by appointment id"""
        pass

    @abstractmethod
    def search_by_staff_id(self,value):
        """search by staff id"""
        pass