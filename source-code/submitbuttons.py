from queries import insert_patient, write_presc, delete_patient, create_appointment, write_medrec
import tkinter as tk
# from login import verify_login
from datetime import *

# LOGGED_IN = False

def submit_patient(fname_entry, lname_entry, gender_entry, age_entry, address_entry, phone_entry, ssn_entry):
    # pat_id = int(patid_entry.get())
    pat_fname = fname_entry.get()
    pat_lname = lname_entry.get()
    pat_age = int(age_entry.get())
    pat_gender = gender_entry.get()
    pat_address = address_entry.get()
    pat_phone = phone_entry.get()
    pat_ssn = ssn_entry.get()
    insert_patient(pat_fname, pat_lname, pat_gender, pat_age, pat_address, pat_phone, pat_ssn)
    #This clears the entries
    # patid_entry.delete(0, tk.END)
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    ssn_entry.delete(0, tk.END)
    
def deletepat_button(patid_entry):
    pat_id = int(patid_entry.get())
    delete_patient(pat_id)
    #This clears the entries
    patid_entry.delete(0, tk.END)

    
def write_prescription(medrec_id_entry, instructions_entry, medication_entry):
    medrec_id = int(medrec_id_entry.get())
    instructions = instructions_entry.get()
    medication = medication_entry.get()
    created = date.today()
    write_presc(medrec_id, instructions, medication, created)
    #This clears the entries
    medrec_id_entry.delete(0, tk.END)
    instructions_entry.delete(0, tk.END)
    medication_entry.delete(0, tk.END)
    
def submit_medrec(patid_entry, empid_entry, symptoms_entry, diagid_entry, procedures_entry, notes_entry):
    pat_id = int(patid_entry.get())
    emp_id = int(empid_entry.get())
    symptoms = symptoms_entry.get()
    diagnosis_id = diagid_entry.get()
    procedures = procedures_entry.get()
    notes = notes_entry.get()
    created = date.today()
    write_medrec(pat_id, emp_id, symptoms, diagnosis_id, procedures, notes, created)
    #This clears the entries
    patid_entry.delete(0, tk.END)
    empid_entry.delete(0, tk.END)
    symptoms_entry.delete(0, tk.END)
    diagid_entry.delete(0, tk.END)
    procedures_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)
    

# ###### LOGIN BUTTON ######
# def submit_login(username_entry, passwd_entry):
#     user = username_entry.get()
#     passwd = passwd_entry.get()
    
#     verified = verify_login(user, passwd)
#     print(verified, "is verified")
    
#     global LOGGED_IN
#     LOGGED_IN = verified

#     #This clears the entries
#     username_entry.delete(0, tk.END)
#     passwd_entry.delete(0, tk.END)
    
#     return verified


###### APPOINTMENT BUTTON ######
def submit_appointment(patient_id_entry, doctor_id_entry, room_id_entry, start_time_entry, end_time_entry):
    pat_id = int(patient_id_entry.get())
    start_time = start_time_entry.get()
    emp_id = int(doctor_id_entry.get())
    room_id = int(room_id_entry.get())
    end_time = end_time_entry.get()
    status = "A"
    cancel_rson = "no"
    create_appointment(pat_id, start_time, emp_id, room_id, end_time, status, cancel_rson)
    patient_id_entry.delete(0, tk.END)
    doctor_id_entry.delete(0, tk.END)
    room_id_entry.delete(0, tk.END)
    start_time_entry.delete(0, tk.END)
    end_time_entry.delete(0, tk.END)


