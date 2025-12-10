from Dao.DoctorAbstract import DoctorAbstract
from Models.patient import Patient
from Models.appointment import Appointment
from DBConnection.ConnectionDB import ConnectionDB
from pymysql.cursors import DictCursor

class DoctorDAOImpl(DoctorAbstract):

    GET_APPOINTMENT_BY_ID = "SELECT * FROM appointment WHERE appointment_id=%s"
    GET_PATIENT_BY_ID = "SELECT * FROM patient WHERE patient_id=%s"

    INSERT_PRESCRIPTION = """INSERT INTO prescription
    (appointment_id, medicine_id, dosage, frequency, duration, quantity)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    def __init__(self):
        self.conn = ConnectionDB().get_connection()

    def get_appointment_by_id(self, appointment_id: int):
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.GET_APPOINTMENT_BY_ID, (appointment_id,))
            row = cursor.fetchone()

            if row:
                return Appointment(
                    appointment_id=row["appointment_id"],
                    appointment_date=row["appointment_date"],
                    appointment_time=row["appointment_time"],
                    token_no=row["token_no"],
                    status=row["status"],
                    patient_id=row["patient_id"],
                    doctor_id=row["doctor_id"]
                )
            return None

        except Exception as e:
            print("Error in get_appointment_by_id:", e)
            return None

    def get_patient_by_id(self, patient_id: int):
        try:
            cursor = self.conn.cursor(DictCursor)
            cursor.execute(self.GET_PATIENT_BY_ID, (patient_id,))
            row = cursor.fetchone()

            if row:
                return Patient(
                    patient_id=row["patient_id"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    gender=row["gender"],
                    DOB=row["DOB"],  
                    age=row["age"],
                    phone=row["phone"],
                    address=row["address"],
                    email=row["email"],
                    created_on=row["created_on"]
                )
            return None

        except Exception as e:
            print("Error in get_patient_by_id:", e)
            return None

    def add_prescription(self, appointment_id, medicine_id,
                         dosage, frequency, duration, quantity) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                self.INSERT_PRESCRIPTION,
                (appointment_id, medicine_id, dosage, frequency, duration, quantity)
            )
            self.conn.commit()
            return cursor.rowcount == 1

        except Exception as e:
            print("Error adding prescription:", e)
            return False

        finally:
            cursor.close()
