from abc import  ABC, abstractmethod
from typing import List 
from Models.medicine import Medicine
class MedicineDaoService(ABC):
    '''create all faetures required'''
    @abstractmethod
    def insert_medicines(self, medicine: Medicine) -> bool:
        '''insert new products'''
        pass
    @abstractmethod
    def display_all_medicines(self) -> List[Medicine]:
        """Fetch/display all medicines"""
        pass

    @abstractmethod
    def search_medicines_by_name(self, name: str) -> List[Medicine]:
        """Search medicines by (partial) name"""
        pass

    @abstractmethod
    def find_by_medicine_id(self, medicine_id: int):
        pass
    
    @abstractmethod
    def update_medicine_quantity(self, medicine_id: int, new_quantity: int) -> bool:
        pass
