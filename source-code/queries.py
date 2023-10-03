import psycopg2
import db_details


#Upates values in the table patient 
# def update_patient():
#     conn = None
#     cur = None
#     try:
#         conn = psycopg2.connect(
#             host = db_details.HOST,
#             database = db_details.DATABASE,
#             user = db_details.USER,
#             password = db_details.PASSWORD,
#             port = db_details.PORT,
#             )
#         cur = conn.cursor()
        
#         update_log = "UPDATE TABLE patient SET name='{patient_name}', age='{patient_age}', time='{patient_time}', WHERE id='{patient_id}'"
#         cur.execute(update_log)
        
#         conn.commit()
#     except Exception as error:
#         print(error)
#     finally:
#         if cur is not None:
#             cur.close()
#         if conn is not None:
#             conn.close()

# TODO: Change delete_pat and delete_medrecs to prepared statements
def delete_patient(pat_id):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            )
        cur = conn.cursor()
        
        delete_appointment = "DELETE FROM appointment WHERE pat_id = %s"
        cur.execute(delete_appointment, (pat_id,))
        delete_prescription = "DELETE FROM prescription WHERE record_id = (SELECT record_id FROM medical_record WHERE pat_id = %s)"
        cur.execute(delete_prescription, (pat_id,))
        delete_medrecs ="DELETE FROM medical_record WHERE pat_id = %s"
        cur.execute(delete_medrecs, (pat_id,))
        delete_pat = "DELETE FROM patient WHERE pat_id = %s"
        cur.execute(delete_pat, (pat_id,))

        conn.commit()
        
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    
#Insert new values into the table patient
def insert_patient(pat_fname, pat_lname, pat_gender, pat_age, pat_address, pat_phone, pat_ssn):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            )
        cur = conn.cursor()
        
        insert_patient = "INSERT INTO patient (f_name, l_name, gender, age, address, phone_num, ssn) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (pat_fname, pat_lname, pat_gender, pat_age, pat_address, pat_phone, pat_ssn)
        cur.execute(insert_patient, values)
        conn.commit()
    
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
            


    
#Write prescription for patient
def write_presc(medrec_id, instructions, medication, created):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            )
        cur = conn.cursor()
        
        insert_prescription = "INSERT INTO prescription (record_id, instructions, created, medication) VALUES (%s, %s, %s, %s)"
        values = (medrec_id, instructions, created, medication)
        cur.execute(insert_prescription, values)
        conn.commit()
        
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()    

#Write a medical record (row)
def write_medrec(pat_id, emp_id, symptoms, diagnosis_id, procedures, notes, created):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            )
        cur = conn.cursor()
        
        insert_prescription = "INSERT INTO medical_record (pat_id, emp_id, symptoms, diag_id, record_procedures, notes, created) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (pat_id, emp_id, symptoms, diagnosis_id, procedures, notes, created)
        cur.execute(insert_prescription, values)
        conn.commit()
    
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    

#Update medical record



def create_appointment(pat_id, start_time, emp_id, room_id, end_time, status, cancel_rson):
    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            )
        cur = conn.cursor()

        insert_appointment = "INSERT INTO appointment (pat_id, start_time, emp_id, room_id, end_time, status, cancel_rson) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (pat_id, start_time, emp_id, room_id, end_time, status, cancel_rson)
        cur.execute(insert_appointment, values)
        conn.commit()
                 
    except Exception as e:
        print(e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

