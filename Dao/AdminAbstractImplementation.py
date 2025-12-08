from Dao.AdminAbstract import AdminDaoServies
from DBConnection.ConnectionDB import ConnectionDB
from Models.staff import Staff


class AdminAbstractImplementation(AdminDaoServies):

    INSERT = "INSERT INTO staff(name, email, phone, status, created_on, role_id) VALUES (%s,%s,%s,%s,%s,%s)"
    UPDATE = "UPDATE staff SET name=%s, email=%s, phone=%s, status=%s, role_id=%s WHERE staff_id=%s"
    SELECT_ALL = "SELECT * FROM staff"
    SELECT_ONE = "SELECT * FROM staff WHERE staff_id=%s"
    DELETE = "DELETE FROM staff WHERE staff_id=%s"

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    # ------------ ADD -------------
    def add_staff(self, staff: Staff):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT, (
                staff.name,
                staff.email,
                staff.phone,
                staff.status,
                staff.created_on,
                staff.role_id
            ))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting staff:", e)
            return False

    # ------------ FIND BY ID -------------
    def find_by_id(self, staff_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.SELECT_ONE, (staff_id,))
            row = cursor.fetchone()

            if row:
                staff = Staff()
                staff.id = row[0]
                staff.name = row[1]
                staff.email = row[2]
                staff.phone = row[3]
                staff.status = row[4]
                staff.created_on = row[5]
                staff.role_id = row[6]
                return staff
            return None
        except Exception as e:
            print("Error fetching staff:", e)
            return None

    # ------------ VIEW ALL -------------
    def view_staff(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.SELECT_ALL)
            rows = cursor.fetchall()
            staff_list = []

            for row in rows:
                staff = Staff()
                staff.id = row[0]
                staff.name = row[1]
                staff.email = row[2]
                staff.phone = row[3]
                staff.status = row[4]
                staff.created_on = row[5]
                staff.role_id = row[6]
                staff_list.append(staff)
            return staff_list
        except Exception as e:
            print("Error viewing staff:", e)
            return None

    # ------------ UPDATE -------------
    def update_staff(self, staff, staff_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE, (
                staff.name,
                staff.email,
                staff.phone,
                staff.status,
                staff.role_id,
                staff_id
            ))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error updating staff:", e)
            return False

    def delete_staff(self, staff_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE staff SET status=%s WHERE staff_id=%s", ("inactive", staff_id))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error deactivating staff:", e)
            return False

