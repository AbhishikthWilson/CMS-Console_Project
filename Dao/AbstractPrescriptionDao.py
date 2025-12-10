from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List

class PrescriptionDaoService(ABC):

    @abstractmethod
    def get_prescription_by_id(self, prescription_id: int) -> Optional[Dict[str, Any]]:
        """Return a single prescription row by id"""
        pass

    @abstractmethod
    def get_all_prescriptions(self) -> List[Dict[str, Any]]:
        """Return all prescription rows"""
        pass
