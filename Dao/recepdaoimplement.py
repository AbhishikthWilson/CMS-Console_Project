from DBConnection.ConnectionDB import ConnectionDB
from Models.Patient import Patient
from Dao.RecepAbstract import PatientDaoService
from pymysql.cursors import DictCursor   

class RecepDaoImplementation(PatientDaoService):
    """implement abstract method here"""
    INSERT_ALL = "INSERT INTO patient(first_name,last_name,gender,DOB,age,phone,address,email,created_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    DISPLAY_BY_ID = "SELECT * FROM patient WHERE patient_id = %s"
    UPDATE_PRODUCT = "UPDATE patient set {field_name} = %s WHERE patient_id = %s"
    
    def __init__(self):
        #get connection object
        self.conn = ConnectionDB().get_connection()
        
    
    # def patient_display_all(self):
    #     """fetch all patients details"""
    #     pass
    
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
        query = self.UPDATE_PRODUCT.format(field_name=field_name)

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

        
               
    