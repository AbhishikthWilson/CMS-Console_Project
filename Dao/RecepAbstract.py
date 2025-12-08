from abc import abstractmethod,ABC

class PatientDaoService(ABC):
    
    @abstractmethod
    def patient_display_all(self):
        pass
    
    @abstractmethod
    def patient_update_by_id(self):
        pass
    
    @abstractmethod
    def patient_search_by_id(self):
        pass
    
    @abstractmethod
    def patient_insert(self):
        pass
    
    @abstractmethod
    def add_appointment(self):
        pass