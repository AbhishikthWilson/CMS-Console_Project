from typing import List
from Models.medicine import Medicine
from Dao.AbstractMedicineDao import MedicineDaoService
from DBConnection.ConnectionDB import ConnectionDB
from pymysql.cursors import DictCursor

class MedicineDaoImplementation(MedicineDaoService):

    # SQL QUERIES
    
    INSERT_MEDICINE = """
        INSERT INTO medicine(medicine_name, category, company_name, quantity, price, expiry_date, created_on)
        VALUES(%s, %s, %s, %s, %s, %s, NOW())
    """
    DISPLAY_ALL = "SELECT * FROM medicine"

    SEARCH_BY_NAME = "SELECT * FROM medicine WHERE medicine_name LIKE %s"

    FIND_BY_ID = "SELECT * FROM medicine WHERE medicine_id = %s"

    UPDATE_QUANTITY = "UPDATE medicine SET quantity=%s WHERE medicine_id=%s"

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    # INSERT (same pattern as Product)
    def insert_medicines(self, medicine: Medicine) -> bool:
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                self.INSERT_MEDICINE,
                (
                    medicine.medicine_name,
                    medicine.category,
                    medicine.company_name,
                    medicine.quantity,
                    medicine.price,
                    medicine.expiry_date
                )
            )
            self.conn.commit()
            return cursor.rowcount == 1
        
        except Exception as e:
            print("Error inserting medicine:", e)
            return False
        
        finally:
            if cursor:
                cursor.close()
    
    # ---------- DISPLAY ALL ----------
    def display_all_medicines(self) -> List[Medicine]:
        medicines: List[Medicine] = []
        cursor = None
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.DISPLAY_ALL)
            rows = cursor.fetchall()
            for row in rows:
                medicines.append(
                    Medicine(
                        medicine_id=row["medicine_id"],
                        medicine_name=row["medicine_name"],
                        category=row["category"],
                        company_name=row["company_name"],
                        quantity=row["quantity"],
                        price=row["price"],
                        expiry_date=row["expiry_date"],
                        created_on=row["created_on"],
                    )
                )
        except Exception as e:
            print("Error fetching medicines:", e)
        finally:
            if cursor:
                cursor.close()
        return medicines
    
    # ---------- SEARCH BY NAME ----------
    def search_medicines_by_name(self, name: str) -> List[Medicine]:
        medicines: List[Medicine] = []
        cursor = None
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.SEARCH_BY_NAME, (f"%{name}%",))
            rows = cursor.fetchall()
            for row in rows:
                medicines.append(
                    Medicine(
                        medicine_id=row["medicine_id"],
                        medicine_name=row["medicine_name"],
                        category=row["category"],
                        company_name=row["company_name"],
                        quantity=row["quantity"],
                        price=row["price"],
                        expiry_date=row["expiry_date"],
                        created_on=row["created_on"],
                    )
                )
        except Exception as e:
            print("Error searching medicines:", e)
        finally:
            if cursor:
                cursor.close()
        return medicines
    
    def find_by_medicine_id(self, medicine_id: int):
        cursor = None
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.FIND_BY_ID, (medicine_id,))
            row = cursor.fetchone()
            if row:
                return Medicine(
                medicine_id=row["medicine_id"],
                medicine_name=row["medicine_name"],
                category=row["category"],
                company_name=row["company_name"],
                quantity=row["quantity"],
                price=row["price"],
                expiry_date=row["expiry_date"],
                created_on=row["created_on"],
            )
            return None

        except Exception as e:
            print("Error finding medicine:", e)
            return None
        finally:
            if cursor:
                cursor.close()

    
    def update_medicine_quantity(self, medicine_id: int, new_quantity: int) -> bool:
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE_QUANTITY, (new_quantity, medicine_id))
            self.conn.commit()
            return cursor.rowcount == 1

        except Exception as e:
            print("Error updating medicine quantity:", e)
            return False

        finally:
            if cursor:
                cursor.close()

    
