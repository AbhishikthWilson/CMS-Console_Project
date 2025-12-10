from typing import Optional, Dict, Any, List
from pymysql.cursors import DictCursor

from Dao.AbstractPrescriptionDao import PrescriptionDaoService
from DBConnection.ConnectionDB import ConnectionDB


class PrescriptionDaoImplementation(PrescriptionDaoService):
    """
    We assume table name: prescription
    Columns: prescription_id, dosage, frequency, duration,
             quantity, appointment_id, medicine_id
    Change table name below if yours is different.
    """

    GET_ONE = """
        SELECT prescription_id, dosage, frequency, duration,
               quantity, appointment_id, medicine_id
        FROM prescription
        WHERE prescription_id = %s
    """

    GET_ALL = """
        SELECT prescription_id, dosage, frequency, duration,
               quantity, appointment_id, medicine_id
        FROM prescription
        ORDER BY prescription_id
    """

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    def get_prescription_by_id(self, prescription_id: int) -> Optional[Dict[str, Any]]:
        cursor = None
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.GET_ONE, (prescription_id,))
            row = cursor.fetchone()
            return row
        except Exception as e:
            print("Error loading prescription:", e)
            return None
        finally:
            if cursor:
                cursor.close()

    def get_all_prescriptions(self) -> List[Dict[str, Any]]:
        cursor = None
        rows: List[Dict[str, Any]] = []
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.GET_ALL)
            rows = cursor.fetchall()
        except Exception as e:
            print("Error loading prescriptions:", e)
        finally:
            if cursor:
                cursor.close()
        return rows
