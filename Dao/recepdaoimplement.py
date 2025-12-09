from DBConnection.ConnectionDB import ConnectionDB
from Models.patient import Patient
from Models.appointment import Appointment
from Models.doctor import Doctor
from Dao.RecepAbstract import PatientDaoService
from pymysql.cursors import DictCursor
from Models.receptionist_billing import ReceptionistBilling
from Models.staff import Staff


class RecepDaoImplementation(PatientDaoService):
    """implement abstract method here"""
    INSERT_ALL = "INSERT INTO patient(first_name,last_name,gender,DOB,age,phone,address,email,created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    DISPLAY_BY_ID = "SELECT * FROM patient WHERE patient_id = %s"
    UPDATE_PATIENT = "UPDATE patient set {field_name} = %s WHERE patient_id = %s"
    SELECT_PATIENT = "SELECT * FROM patient"    
    INSERT_APP = "INSERT INTO appointment(appointment_date, appointment_time, token_no, status, patient_id, doctor_id) VALUES (%s,%s,%s,%s,%s,%s)"
    DISPLAY_BY_Doc_ID = "SELECT * FROM doctor WHERE doctor_id = %s"
    SELECT_APP = "SELECT * FROM appointment ORDER BY appointment_date, appointment_time"
    INSERT_BILL = "INSERT INTO receptionist_billing(total_amount, bill_date, appointment_id, staff_id) VALUES (%s,%s,%s,%s)"
    DISPLAY_BY_APP_ID = "SELECT * FROM appointment WHERE appointment_id = %s"
    DISPLAY_BY_STAFF_ID = "SELECT * FROM staff WHERE staff_id = %s"



    def __init__(self):
        #get connection object
        self.conn = ConnectionDB().get_connection()
        
    
    def patient_display_all(self):
        """fetch all patients details"""
        #to store the records from database
        #create a empty list
        patient = []
        cursor = None
        
        try:
            cursor = self.conn.cursor(DictCursor)
            #return data in dict format
            cursor.execute(self.SELECT_PATIENT)
            #fire the query
            rows = cursor.fetchall()
            for row in rows:
                patient.append(Patient(patient_id=row["patient_id"],
                                        first_name=row["first_name"],
                                        last_name=row["last_name"],
                                        gender=row["gender"],
                                        DOB=row["DOB"],
                                        age=row["age"],
                                        phone=row["phone"],
                                        address=row["address"],
                                        email=row["email"],
                                        created_on=row["created_on"]))        
        
        except Exception as e:
            print("error fetching appointment:",e)
            
        finally:
            cursor.close()
        return patient
    
    def add_patient(self,patient:Patient):
        """Add patient details"""
        try:
            cursor = self.conn.cursor() #create a cursor object
            cursor.execute(self.INSERT_ALL,(patient.first_name,
                                                patient.last_name,
                                                patient.gender,
                                                patient.DOB,
                                                patient.age,
                                                patient.phone,
                                                patient.address,
                                                patient.email,
                                                patient.created_on)) 
            
            self.conn.commit()#added to db table
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting patient:",e)
            return False
        finally:
            cursor.close()
            
            
    def search_by_patient_id(self,value):
        """search by patient id"""
        patient = None
        cursor = None
        
        try:
            cursor = self.conn.cursor(DictCursor)
            #return data in dic format
            cursor.execute(self.DISPLAY_BY_ID,(value,))
            #fire the query
            row = cursor.fetchone()
            
            if row:
                patient = Patient(patient_id=row["patient_id"],
                                  first_name=row["first_name"],
                                  last_name=row["last_name"],
                                    gender=row["gender"],
                                    DOB=row["DOB"],
                                    age=row["age"],
                                    phone=row["phone"],
                                    address=row["address"],
                                    email=row["email"],
                                    created_on=row["created_on"])          
        
        except Exception as e:
            print("error fetching patient:",e)
            
        finally:
            cursor.close()
        return patient
    
    
    def update_patient(self, patient: Patient, patient_id: int, field_name: str):
        """Update patient by id"""

        # Get the new value from the Patient object
        value = getattr(patient, field_name, None)

        if value is None:
            print("Invalid field name:", field_name)
            return False

        # Build SQL with the correct column
        query = self.UPDATE_PATIENT.format(field_name=field_name)

        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (value, patient_id))
            self.conn.commit()
            return cursor.rowcount == 1

        except Exception as e:
            print("Error inserting patient:", e)
            return False

        finally:
            cursor.close()
    
    
    def add_appointment(self, appointment: Appointment):
        """Add patient details"""
        try:
            cursor = self.conn.cursor() #create a cursor object
            cursor.execute(self.INSERT_APP,(appointment.appointment_date,
                                                appointment.appointment_time,
                                                appointment.token_no,
                                                appointment.status,
                                                appointment.patient_id,
                                                appointment.doctor_id)) 
            
            self.conn.commit()#added to db table
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting appointment:",e)
            return False
        finally:
            cursor.close()
        

    def search_by_doctor_id(self,value):
        """search by doctor id"""
        doctor = None
        cursor = None
        
        try:
            cursor = self.conn.cursor(DictCursor)
            #return data in dic format
            cursor.execute(self.DISPLAY_BY_Doc_ID,(value,))
            #fire the query
            row = cursor.fetchone()
            
            if row:
                doctor = Doctor(doctor_id=row["doctor_id"],
                                  specialization=row["specialization"],
                                  doctor_fee=row["doctor_fee"],
                                    working_time=row["working_time"],
                                    staff_id=row["staff_id"])          
        
        except Exception as e:
            print("error fetching doctor:",e)
            
        finally:
            cursor.close()
        return doctor 


    def view_appointment(self):
        """view appointment"""
        #to store the records from database
        #create a empty list
        appointment = []
        cursor = None
        
        try:
            cursor = self.conn.cursor(DictCursor)
            #return data in dict format
            cursor.execute(self.SELECT_APP)
            #fire the query
            rows = cursor.fetchall()
            for row in rows:
                appointment.append(Appointment(appointment_id=row["appointment_id"],
                                        appointment_date=row["appointment_date"],
                                        appointment_time=row["appointment_time"],
                                        token_no=row["token_no"],
                                        status=row["status"],
                                        patient_id=row["patient_id"],
                                        doctor_id=row["doctor_id"]))        
        
        except Exception as e:
            print("error fetching appointment:",e)
            
        finally:
            cursor.close()
        return appointment 

    def payment_and_billing(self,billing:ReceptionistBilling):
        """payment and billing"""
        try:
            cursor = self.conn.cursor() #create a cursor object
            cursor.execute(self.INSERT_BILL,(billing.total_amount,
                                                billing.bill_date,
                                                billing.appointment_id,
                                                billing.staff_id)) 
            
            self.conn.commit()#added to db table
            return cursor.rowcount == 1
        except Exception as e:
            print("Error inserting billing:",e)
            return False
        finally:
            cursor.close() 

    def search_by_appointment_id(self,value):
        """search by appointment id"""
        appointment = None
        cursor = None
        
        try:
            cursor = self.conn.cursor(DictCursor)
            #return data in dic format
            cursor.execute(self.DISPLAY_BY_APP_ID,(value,))
            #fire the query
            row = cursor.fetchone()
            
            if row:
                appointment = Appointment(appointment_id=row["appointment_id"],
                                  appointment_date=row["appointment_date"],
                                  appointment_time=row["appointment_time"],
                                    token_no=row["token_no"],
                                    status=row["status"],
                                    patient_id=row["patient_id"],
                                    doctor_id=row["doctor_id"])          
        
        except Exception as e:
            print("error fetching appointment:",e)
            
        finally:
            cursor.close()
        return appointment             
    
    def search_by_staff_id(self,value):
        """search by staff id"""
        staff = None
        cursor = None
        
        try:
            cursor = self.conn.cursor(DictCursor)
            #return data in dic format
            cursor.execute(self.DISPLAY_BY_STAFF_ID,(value,))
            #fire the query
            row = cursor.fetchone()
            
            if row:
                staff = Staff(staff_id=row["staff_id"],
                                  name=row["name"],
                                  email=row["email"],
                                    phone=row["phone"],
                                    status=row["status"],
                                    created_on=row["created_on"],
                                    role_id=row["role_id"])          
        
        except Exception as e:
            print("error fetching staff:",e)  
            
        finally:
            cursor.close()
        return staff 