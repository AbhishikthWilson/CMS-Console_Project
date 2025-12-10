from abc import ABC, abstractmethod
from Models.appointment import Appointment
from Models.patient import Patient
from typing import List

class DoctorAbstract(ABC):

    @abstractmethod
    def get_appointment_by_id(self, appointment_id:int)->Appointment:
        '''view appoinment'''
        pass

    @abstractmethod
    def get_patient_by_id(self, patient_id:int)->Patient:
        '''view patient'''
        pass
@abstractmethod
def add_prescription(self, appointment_id, medicine_id,
                     dosage, frequency, duration, quantity) -> bool:
    pass

  

