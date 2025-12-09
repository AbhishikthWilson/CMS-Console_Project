from typing import List, Dict, Any, Optional
from pymysql.cursors import DictCursor

from Dao.AbstractBillDao import BillDaoService
from DBConnection.ConnectionDB import ConnectionDB


class BillDaoImplementation(BillDaoService):
    """
    Tables used:
      medicine_bill       : bill_id, item_id, total_amount, bill_date
      prescription_item   : item_id, prescription_id
      prescription        : prescription_id, dosage, frequency, duration, quantity, appointment_id, medicine_id
      medicine            : medicine_id, medicine_name, category, company_name, quantity, price, expiry_date, created_on
    """

    INSERT_ITEM = "INSERT INTO prescription_item (prescription_id) VALUES (%s)"

    INSERT_BILL = """
        INSERT INTO medicine_bill (item_id, total_amount, bill_date)
        VALUES (%s, %s, NOW())
    """

    GET_ALL_BILLS = """
        SELECT 
            b.bill_id,
            b.bill_date,
            b.total_amount,
            pi.item_id,
            p.prescription_id,
            p.quantity,
            m.medicine_name
        FROM medicine_bill b
        JOIN prescription_item pi ON b.item_id = pi.item_id
        JOIN prescription p ON pi.prescription_id = p.prescription_id
        JOIN medicine m ON p.medicine_id = m.medicine_id
        ORDER BY b.bill_id DESC
    """

    GET_BILL_DETAILS = """
        SELECT 
            b.bill_id,
            b.bill_date,
            b.total_amount,
            pi.item_id,
            p.prescription_id,
            p.dosage,
            p.frequency,
            p.duration,
            p.quantity,
            m.medicine_id,
            m.medicine_name,
            m.price
        FROM medicine_bill b
        JOIN prescription_item pi ON b.item_id = pi.item_id
        JOIN prescription p ON pi.prescription_id = p.prescription_id
        JOIN medicine m ON p.medicine_id = m.medicine_id
        WHERE b.bill_id = %s
    """

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    def create_bill_for_prescription(self, prescription_id: int, total_amount: float) -> bool:
        cursor = None
        try:
            cursor = self.conn.cursor()

            # Insert into prescription_item
            cursor.execute(self.INSERT_ITEM, (prescription_id,))
            item_id = cursor.lastrowid

            # Insert into medicine_bill
            cursor.execute(self.INSERT_BILL, (item_id, total_amount))

            self.conn.commit()
            return True
        except Exception as e:
            print("Error while creating bill:", e)
            self.conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def get_all_bills(self) -> List[Dict[str, Any]]:
        cursor = None
        rows: List[Dict[str, Any]] = []
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.GET_ALL_BILLS)
            rows = cursor.fetchall()
        except Exception as e:
            print("Error fetching bills:", e)
        finally:
            if cursor:
                cursor.close()
        return rows

    def get_bill_details(self, bill_id: int) -> Optional[Dict[str, Any]]:
        cursor = None
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.GET_BILL_DETAILS, (bill_id,))
            row = cursor.fetchone()
            return row
        except Exception as e:
            print("Error fetching bill detail:", e)
            return None
        finally:
            if cursor:
                cursor.close()


