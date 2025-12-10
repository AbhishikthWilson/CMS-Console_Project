from Dao.DoctorDaoServices import DoctorDaoServices
from DBConnection.ConnectionDB import ConnectionDB
from Models.doctor import Doctor

class DoctorDaoImplementation(DoctorDaoServices):

    INSERT = "INSERT INTO doctor(specialization, doctor_fee, working_time, staff_id) VALUES (%s,%s,%s,%s)"
    UPDATE = "UPDATE doctor SET specialization=%s, doctor_fee=%s, working_time=%s, staff_id=%s WHERE doctor_id=%s"
    SELECT_ALL = "SELECT * FROM doctor"
    SELECT_ONE = "SELECT * FROM doctor WHERE doctor_id=%s"

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    def add_doctor(self, doctor):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.INSERT, (
                doctor.specialization,
                doctor.doctor_fee,
                doctor.working_time,
                doctor.staff_id,
            ))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting doctor:", e)
            return False

    def find_by_id(self, doctor_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.SELECT_ONE, (doctor_id,))
            row = cursor.fetchone()
            if row:
                d = Doctor()
                d.doctor_id = row[0]
                d.specialization = row[1]
                d.doctor_fee = row[2]
                d.working_time = row[3]
                d.staff_id = row[4]
                return d
            return None
        except Exception as e:
            print("Error fetching doctor:", e)
            return None

    def view_doctors(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.SELECT_ALL)
            rows = cursor.fetchall()
            doctor_list = []

            for row in rows:
                d = Doctor()
                d.doctor_id = row[0]
                d.specialization = row[1]
                d.doctor_fee = row[2]
                d.working_time = row[3]
                d.staff_id = row[4]
                doctor_list.append(d)
            return doctor_list
        except Exception as e:
            print("Error viewing doctors:", e)
            return None

    def update_doctor(self, doctor, doctor_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(self.UPDATE, (
                doctor.specialization,
                doctor.doctor_fee,
                doctor.working_time,
                doctor.staff_id,
                doctor_id
            ))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error updating doctor:", e)
            return False

    def delete_doctor(self, doctor_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE doctor SET status='inactive' WHERE doctor_id=%s", (doctor_id,))
            self.conn.commit()
            return cursor.rowcount == 1
        except Exception as e:
            print("Error deactivating doctor:", e)
            return False
