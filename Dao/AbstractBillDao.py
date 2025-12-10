from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class BillDaoService(ABC):

    @abstractmethod
    def create_bill_for_prescription(self, prescription_id: int, total_amount: float) -> bool:
        """
        Creates:
          1) a row in item table (item_id, prescription_id)
          2) a row in bill table (bill_id, item_id, total_amount, bill_date)
        """
        pass

    @abstractmethod
    def get_all_bills(self) -> List[Dict[str, Any]]:
        """Return list of all bills (with medicine summary)"""
        pass

    @abstractmethod
    def get_bill_details(self, bill_id: int) -> Optional[Dict[str, Any]]:
        """Return detailed information for one bill"""
        pass
