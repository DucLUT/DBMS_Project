import tkinter as tk
from submitbuttons import submit_patient, write_prescription, deletepat_button, submit_appointment, submit_medrec
from login import verify_login
import db_details
import psycopg2
import os
import json

LOGGED_IN = False

root = tk.Tk()
width = root.winfo_screenwidth()-10
height = root.winfo_screenheight()-10
root.geometry("%dx%d" % (width, height))
root.title("Hospital database")

ArialSmall = ('Arial', 14)
ArialTiny = ('Arial', 10)
ArialTinyBold = ('Arial Bold', 10)
ArialBig = ('Arial', 20)

LightBlue = '#CDDEEE'
DarkerBlue = '#84CBCB'

#Here's the main frame/pages 
#The welcome page's frame
def welcome_page():
    welcome_frame = tk.Frame(main_frame)
    print(os.getcwd())
    
    lb = tk.Label(welcome_frame, text='Welcome!', font=ArialBig)
    lb.pack()
    
    def submit_pwd(insertdbpwd_entry):
        password = insertdbpwd_entry.get()
        
        cwd = os.getcwd()
        json_path = os.path.join(cwd, 'connection_config.json')
        
        with open(json_path, 'r') as f:
            config = json.load(f)
        
        config['PASSWORD'] = password
        
        with open(json_path, 'w') as f:
            json.dump(config, f)
            
        try:
            conn = psycopg2.connect(
                host = db_details.HOST,
                database = db_details.DATABASE,
                user = db_details.USER,
                password = password,
                port = db_details.PORT,
            )
            cur = conn.cursor()
        
            print("connection succesful")
            
            connection_label = tk.Label(welcome_frame, text='Connection succesful')
            connection_label.pack()
        except Exception as e:
            print(f"connection not succesful: {str(e)}")
            connection_label = tk.Label(welcome_frame, text="Connection not succesful")
            connection_label.pack()
    
    insertdbpwd_label = tk.Label(welcome_frame, text='Insert your database password here\nwhich you use to access databases')
    insertdbpwd_label.pack()
    
    insertdbpwd_entry = tk.Entry(welcome_frame)
    insertdbpwd_entry.pack()

    submit_button = tk.Button(welcome_frame, text="Submit", command=lambda: submit_pwd(insertdbpwd_entry))
    submit_button.pack()
    
    welcome_frame.pack(pady=20, padx=20)
    
#Add patient here
def patient_page():
    patient_frame = tk.Frame(main_frame, bg = LightBlue)
    
    lb = tk.Label(patient_frame, text="Add a patient", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=1) 
    
    fname_label = tk.Label(patient_frame, text="First name:", font=ArialSmall, bg=LightBlue)
    fname_label.grid(row=2, column=0, pady=10, padx=10)

    fname_entry = tk.Entry(patient_frame, font=ArialSmall)
    fname_entry.grid(row=2, column=1, pady=10, padx=10)

    lname_label = tk.Label(patient_frame, text="Last name:", font=ArialSmall, bg=LightBlue)
    lname_label.grid(row=3, column=0, pady=10, padx=10)

    lname_entry = tk.Entry(patient_frame, font=ArialSmall)
    lname_entry.grid(row=3, column=1, pady=10, padx=10)

    age_label = tk.Label(patient_frame, text="Age:", font=ArialSmall, bg=LightBlue)
    age_label.grid(row=4, column=0, pady=10, padx=10)

    age_entry = tk.Entry(patient_frame, font=ArialSmall)
    age_entry.grid(row=4, column=1, pady=10, padx=10)

    gender_label = tk.Label(patient_frame, text="Gender:", font=ArialSmall, bg=LightBlue)
    gender_label.grid(row=5, column=0, pady=10, padx=10)

    gender_entry = tk.Entry(patient_frame, font=ArialSmall)
    gender_entry.grid(row=5, column=1, pady=10, padx=10)

    address_label = tk.Label(patient_frame, text="Address:", font=ArialSmall, bg=LightBlue)
    address_label.grid(row=6, column=0, pady=10, padx=10)

    address_entry = tk.Entry(patient_frame, font=ArialSmall)
    address_entry.grid(row=6, column=1, pady=10, padx=10)

    phone_label = tk.Label(patient_frame, text="Phone number:", font=ArialSmall, bg=LightBlue)
    phone_label.grid(row=7, column=0, pady=10, padx=10)

    phone_entry = tk.Entry(patient_frame, font=ArialSmall)
    phone_entry.grid(row=7, column=1, pady=10, padx=10)

    ssn_label = tk.Label(patient_frame, text="SSN:", font=ArialSmall, bg=LightBlue)
    ssn_label.grid(row=8, column=0, pady=10, padx=10)

    ssn_entry = tk.Entry(patient_frame, font=ArialSmall)
    ssn_entry.grid(row=8, column=1, pady=10, padx=10)
    
    submit_button = tk.Button(patient_frame, text="Submit", command=lambda: submit_patient(fname_entry, lname_entry, gender_entry, age_entry, address_entry, phone_entry, ssn_entry))
    submit_button.grid(row=9, column=1, pady=10, padx=10)
    
    lb_delete = tk.Label(patient_frame, text="\nIf you would like to delete a patient:\nInsert the patient's ID\nand press the button below", font=ArialSmall, bg=LightBlue)
    lb_delete.grid(row=10, column=1) 
    
    patid_label = tk.Label(patient_frame, text="ID:", font=ArialSmall, bg=LightBlue)
    patid_label.grid(row=11, column=0, pady=10, padx=10)

    patid_entry = tk.Entry(patient_frame, font=ArialSmall)
    patid_entry.grid(row=11, column=1, pady=10, padx=10)
    
    delete_button = tk.Button(patient_frame, text="Delete", command=lambda: deletepat_button(patid_entry))
    delete_button.grid(row=12, column=1, pady=10, padx=10)
    
    query_label = tk.Label(patient_frame, text="If you'd like to see all of the data in\nthe table patients, press the button below", font=ArialSmall, bg=LightBlue)
    query_label.grid(row=13, column=1, pady=10, padx=10)
    
    queryname_label = tk.Label(patient_frame, text="You can query patients by last name.\nElse leave the field empty.", font=ArialSmall, bg=LightBlue)
    queryname_label.grid(row=14, column=1, pady=10, padx=10)
    
    queryname_entry = tk.Entry(patient_frame, font=ArialSmall)
    queryname_entry.grid(row=15, column=1, pady=10, padx=10)
    
    def querypats():
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
            
            patname = queryname_entry.get()
            if len(patname) < 1:
                query_patients = "SELECT * FROM patient"
            else:
                query_patients = f"SELECT * FROM patient WHERE l_name = %s"
            cur.execute(query_patients, (patname,))
            results  = cur.fetchall()
            
            top = tk.Toplevel()
            top.title("Patient Data")
            top.geometry("1200x300")
            
            canvas = tk.Canvas(top)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar = tk.Scrollbar(top, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.configure(yscrollcommand=scrollbar.set)
            
            rec_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=rec_frame, anchor='nw')
            
            
            column_names = [desc[0] for desc in cur.description]
            for i, name in enumerate(column_names):
                entry = tk.Entry(rec_frame)
                entry.insert(tk.END, name)
                entry.config(state='readonly', font=ArialTinyBold)
                entry.grid(row=0, column=i)

            for i, row in enumerate(results):
                for j, value in enumerate(row):
                    entry = tk.Entry(rec_frame)
                    entry.insert(tk.END, value)
                    entry.config(font=ArialTiny)
                    entry.grid(row=i+1, column=j)
                    
            def on_frame_configure(event):
                canvas.configure(scrollregion=canvas.bbox('all'))
            rec_frame.bind('<Configure>', on_frame_configure)
                
        except Exception as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()          
                
    query_button = tk.Button(patient_frame, text="Query", command=querypats)
    query_button.grid(row=16, column=1, pady=10, padx=10)
        
    patient_frame.pack(pady=20, padx=20)
    
#Write prescription here
def presc_page():
    presc_frame = tk.Frame(main_frame, bg=LightBlue)
    
    lb = tk.Label(presc_frame, text="Write a prescription", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=1)

    medrec_id_label = tk.Label(presc_frame, text="Medical record ID:", font=ArialSmall, bg=LightBlue)
    medrec_id_label.grid(row=2, column=0, pady=10, padx=10)

    medrec_id_entry = tk.Entry(presc_frame, font=ArialSmall)
    medrec_id_entry.grid(row=2, column=1, pady=10, padx=10)

    instructions_label = tk.Label(presc_frame, text="Instructions:", font=ArialSmall, bg=LightBlue)
    instructions_label.grid(row=3, column=0, pady=10, padx=10)

    instructions_entry = tk.Entry(presc_frame, font=ArialSmall)
    instructions_entry.grid(row=3, column=1, pady=10, padx=10)

    medication_label = tk.Label(presc_frame, text="medication:", font=ArialSmall, bg=LightBlue)
    medication_label.grid(row=4, column=0, pady=10, padx=10)
    
    medication_entry = tk.Entry(presc_frame, font=ArialSmall)
    medication_entry.grid(row=4, column=1, pady=10, padx=10)
    
    submit_button = tk.Button(presc_frame, text="Submit", command=lambda: write_prescription(medrec_id_entry, instructions_entry, medication_entry))
    submit_button.grid(row=7, column=2, pady=10, padx=10)
    
    presc_frame.pack(pady=20, padx=20)
  
#Query medical records  
def qmedrec_page():
    qmedrec_frame = tk.Frame(main_frame, bg=LightBlue)
    
    lb = tk.Label(qmedrec_frame, text="Here you can see medical records", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=0)
    
    patid_label = tk.Label(qmedrec_frame, text="Patient's ID", font=ArialSmall, bg=LightBlue)
    patid_label.grid(row=1, column=0, pady=10, padx=10)

    patid_entry = tk.Entry(qmedrec_frame, font=ArialSmall)
    patid_entry.grid(row=2, column=0, pady=10, padx=10)
    
    error_label = tk.Label(qmedrec_frame, text="", font=ArialSmall, bg=LightBlue)
    error_label.grid(row=7, column=0, pady=10, padx=10)
    
    result_frame = tk.Frame(qmedrec_frame, width=1300, height=500)
    result_frame.grid(row=6, column=0, pady=10, padx=10)
    
    canvas = tk.Canvas(result_frame, width=1300, height=500)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    
    result_inner_frame = tk.Frame(canvas, width=1300, height=500)
    canvas.create_window((0, 0), window=result_inner_frame, anchor=tk.NW)
    
    def configure_scroll(event):
        canvas.config(scrollregion=canvas.bbox(tk.ALL))
        
    result_inner_frame.bind("<Configure>", configure_scroll)
        
    def get_medrec():
        conn = psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            )
        cur = conn.cursor()
        
        pat_id = patid_entry.get()
        query_medrec = ""
        if queryall_var.get() == True:
            query_medrec = "SELECT * FROM medical_record"
            cur.execute(query_medrec)
        else:
            query_medrec = f"SELECT * FROM medical_record WHERE pat_id = '{pat_id}'"
            cur.execute(query_medrec, (pat_id,))
        results  = cur.fetchall()
        
        error_label.config(text="")
        canvas.config(scrollregion=canvas.bbox("all"))
        
        for i in range(50):
            tk.Label(result_inner_frame, text="Result {}".format(i)).grid(row=i, column=0, sticky="w", padx=5, pady=5)

        
        if len(results) < 1:
            error_label.config(text="No results found.\nTry another ID")
            for widget in result_inner_frame.winfo_children():
                widget.destroy()
        else:        
            for widget in result_inner_frame.winfo_children():
                widget.destroy()
            
            column_names = [desc[0] for desc in cur.description]
            
            for i, column_names in enumerate(column_names):
                label = tk.Label(result_inner_frame, text=column_names, font=ArialSmall)
                label.grid(row=0, column=i, padx=5, pady=5)
                
                for j, row in enumerate(results):
                    if column_names in ("symptoms", "diag_id", "record_procedures", "notes"):
                        resultbox = tk.Text(result_inner_frame, font=ArialSmall, height=5, width=20)
                        resultbox.insert("1.0", row[i])
                    elif column_names in ("created"):
                        resultbox = tk.Text(result_inner_frame, font=ArialSmall, height=1, width=10)
                        resultbox.insert("1.0", row[i])
                    else:
                        resultbox = tk.Text(result_inner_frame, font=ArialSmall, height=1, width=5)
                        resultbox.insert("1.0", row[i])
                    resultbox.config(state="disabled")
                    resultbox.grid(row=j+1, column=i, padx=5, pady=5)
    
    queryall_var = tk.BooleanVar(value=False)
    queryall_checkbox = tk.Checkbutton(qmedrec_frame, text= "Select all patients", font=ArialSmall, bg=LightBlue, variable=queryall_var)
    queryall_checkbox.grid(row=3, column=0, pady=10, padx=10)
    
    submit_button = tk.Button(qmedrec_frame, text="Query patient", command=get_medrec)
    submit_button.grid(row=4, column=0, pady=10, padx=10)
    
    qmedrec_frame.pack(pady=20, padx=20)
    
#Write a medical record here
def wmedrec_page():
    wmedrec_frame = tk.Frame(main_frame, bg=LightBlue)
    
    lb = tk.Label(wmedrec_frame, text="Here you can write a medical record", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=1) 
    
    patid_label = tk.Label(wmedrec_frame, text="Patient ID:", font=ArialSmall, bg=LightBlue)
    patid_label.grid(row=2, column=0, pady=10, padx=10)

    patid_entry = tk.Entry(wmedrec_frame, font=ArialSmall)
    patid_entry.grid(row=2, column=1, pady=10, padx=10)

    empid_label = tk.Label(wmedrec_frame, text="Employee ID:", font=ArialSmall, bg=LightBlue)
    empid_label.grid(row=3, column=0, pady=10, padx=10)

    empid_entry = tk.Entry(wmedrec_frame, font=ArialSmall)
    empid_entry.grid(row=3, column=1, pady=10, padx=10)

    symptoms_label = tk.Label(wmedrec_frame, text="Symptoms:", font=ArialSmall, bg=LightBlue)
    symptoms_label.grid(row=4, column=0, pady=10, padx=10)

    symptoms_entry = tk.Entry(wmedrec_frame, font=ArialSmall)
    symptoms_entry.grid(row=4, column=1, pady=10, padx=10)

    diagid_label = tk.Label(wmedrec_frame, text="Diagnosis:", font=ArialSmall, bg=LightBlue)
    diagid_label.grid(row=5, column=0, pady=10, padx=10)

    diagid_entry = tk.Entry(wmedrec_frame, font=ArialSmall)
    diagid_entry.grid(row=5, column=1, pady=10, padx=10)

    procedures_label = tk.Label(wmedrec_frame, text="Procedures:", font=ArialSmall, bg=LightBlue)
    procedures_label.grid(row=6, column=0, pady=10, padx=10)

    procedures_entry = tk.Entry(wmedrec_frame, font=ArialSmall)
    procedures_entry.grid(row=6, column=1, pady=10, padx=10)

    notes_label = tk.Label(wmedrec_frame, text="Notes:", font=ArialSmall, bg=LightBlue)
    notes_label.grid(row=7, column=0, pady=10, padx=10)

    notes_entry = tk.Entry(wmedrec_frame, font=ArialSmall)
    notes_entry.grid(row=7, column=1, pady=10, padx=10)
    
    submit_button = tk.Button(wmedrec_frame, text="Submit", command=lambda: submit_medrec(patid_entry, empid_entry, symptoms_entry, diagid_entry, procedures_entry, notes_entry,))
    submit_button.grid(row=4, column=2, pady=10, padx=10)
    
    wmedrec_frame.pack(pady=20, padx=20)
    
#Update a medical record here
def umedrec_page():
    umedrec_frame = tk.Frame(main_frame, bg=LightBlue)
    
    lb = tk.Label(umedrec_frame, text="Update a medical record", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=0)  
    
    recordid_label = tk.Label(umedrec_frame, text="\nInsert record ID:", font=ArialSmall, bg=LightBlue)
    recordid_label.grid(row=1, column=0)
    
    recordid_entry = tk.Entry(umedrec_frame, font=ArialSmall)
    recordid_entry.grid(row=2, column=0)
    
    #Checkboxes
    checkbox_frame = tk.Frame(umedrec_frame, bg=DarkerBlue)
    checkbox_frame.grid(row=3, column=0, pady=10, padx=10)
    
    checkbox_label = tk.Label(checkbox_frame, text="Check one checkbox\nwhich you want to update", bg=DarkerBlue)
    checkbox_label.pack()
    
    notes_var = tk.BooleanVar()
    notes_checkbox = tk.Checkbutton(checkbox_frame, text="Notes", variable=notes_var, bg=DarkerBlue)
    notes_checkbox.pack()
    
    symptoms_var = tk.BooleanVar()
    symptoms_checkbox = tk.Checkbutton(checkbox_frame, text="Symptoms", variable=symptoms_var, bg=DarkerBlue)
    symptoms_checkbox.pack()
    
    diagnosis_var = tk.BooleanVar()
    diagnosis_checkbox = tk.Checkbutton(checkbox_frame, text="Diagnosis", variable=diagnosis_var, bg=DarkerBlue)
    diagnosis_checkbox.pack()
    
    procedure_var = tk.BooleanVar()
    procedure_checkbox = tk.Checkbutton(checkbox_frame, text="Procedure", variable=procedure_var, bg=DarkerBlue)
    procedure_checkbox.pack()
    
    modification_label = tk.Label(umedrec_frame, text="Update text", font=ArialSmall, bg=LightBlue)
    modification_label.grid(row=4, column=0, pady=10, padx=10)
    
    modification_text = tk.Text(umedrec_frame, width=50, height=10)
    modification_text.grid(row=5, column=0)
    
    def update_medrec(notes_var, symptoms_var, diagnosis_var, procedure_var, modification_text, record_id):
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
            if notes_var.get() == True:
                update_rec = f"UPDATE medical_record SET notes = '{modification_text.get('1.0', tk.END)}' WHERE record_id = '{record_id}'"
            elif symptoms_var.get() == True:
                update_rec = f"UPDATE medical_record SET symptoms = '{modification_text.get('1.0', tk.END)}' WHERE record_id = '{record_id}'"
            elif procedure_var.get() == True:
                update_rec = f"UPDATE medical_record SET record_procedures = '{modification_text.get('1.0', tk.END)}' WHERE record_id = '{record_id}'"
            elif diagnosis_var.get() == True:
                update_rec = f"UPDATE medical_record SET diag_id = '{modification_text.get('1.0', tk.END)}' WHERE record_id = '{record_id}'"
        
            cur.execute(update_rec)
            conn.commit()
        except Exception as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
    

    submit_button = tk.Button(umedrec_frame, text="Submit", command=lambda: update_medrec(notes_var, symptoms_var, diagnosis_var, procedure_var, modification_text, int(recordid_entry.get())))
    submit_button.grid(row=4, column=2, pady=10, padx=10)
    
    umedrec_frame.pack(pady=20, padx=20)
    
def appointment_page():
    appointment_frame = tk.Frame(main_frame, bg=LightBlue)
    
    lb = tk.Label(appointment_frame, text="Schedule appointment", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=1) 
    
    # create the patient ID entry widget
    patient_id_label = tk.Label(appointment_frame, text="Patient ID:", font=ArialSmall, bg=LightBlue)
    patient_id_label.grid(row=1, column=0, pady=10, padx=10)
    patient_id_entry = tk.Entry(appointment_frame, font=ArialSmall)
    patient_id_entry.grid(row=1, column=1, pady=10, padx=10)

    # create the doctor ID entry widget
    doctor_id_label = tk.Label(appointment_frame, text="Employee ID:", font=ArialSmall, bg=LightBlue)
    doctor_id_label.grid(row=2, column=0, pady=10, padx=10)
    doctor_id_entry = tk.Entry(appointment_frame, font=ArialSmall)
    doctor_id_entry.grid(row=2, column=1, pady=10, padx=10)

    # create the room ID entry widget
    room_id_label = tk.Label(appointment_frame, text="Room ID:", font=ArialSmall, bg=LightBlue)
    room_id_label.grid(row=3, column=0, pady=10, padx=10)
    room_id_entry = tk.Entry(appointment_frame, font=ArialSmall)
    room_id_entry.grid(row=3, column=1, pady=10, padx=10)

    # create the start time entry widget
    start_time_label = tk.Label(appointment_frame, text='Start Time (YYYY-MM-DD HH:MM:SS):', font=ArialSmall, bg=LightBlue)
    start_time_label.grid(row=4, column=0, pady=10, padx=10)
    start_time_entry = tk.Entry(appointment_frame, font=ArialSmall)
    start_time_entry.grid(row=4, column=1, pady=10, padx=10)
    
    # create the end time entry widget
    end_time_label = tk.Label(appointment_frame, text='End Time (YYYY-MM-DD HH:MM:SS):', font=ArialSmall, bg=LightBlue)
    end_time_label.grid(row=5, column=0, pady=10, padx=10)
    end_time_entry = tk.Entry(appointment_frame, font=ArialSmall)
    end_time_entry.grid(row=5, column=1, pady=10, padx=10)
    
    # Schedule button
    appointment_submit_button = tk.Button(appointment_frame, text="Schedule", command=lambda: submit_appointment(patient_id_entry, doctor_id_entry, room_id_entry, start_time_entry, end_time_entry))
    appointment_submit_button.grid(row=6, column=1, pady=10, padx=10)
    
    joinquery_label = tk.Label(appointment_frame, text='To see your own appointments, enter your Emp IP\nand press "Your appointments"', font=ArialSmall, bg=LightBlue)
    joinquery_label.grid(row=7, column=1, pady=10, padx=10)
    
    empid_label = tk.Label(appointment_frame, text="Employee ID", font=ArialSmall, bg=LightBlue)
    empid_label.grid(row=8, column=0, pady=10, padx=10)
    empid_entry = tk.Entry(appointment_frame, font=ArialSmall)
    empid_entry.grid(row=8, column=1, pady=10, padx=10)
    
    def joinappointments():
        try:
            conn = psycopg2.connect(
                host = db_details.HOST,
                database = db_details.DATABASE,
                user = db_details.USER,
                password = db_details.PASSWORD,
                port = db_details.PORT,
                )
            cur = conn.cursor()
            
            empid = empid_entry.get()
            
            query_join = "SELECT appointment.start_time, patient.f_name, employee.f_name FROM patient INNER JOIN appointment ON patient.pat_id = appointment.pat_id INNER JOIN employee ON appointment.emp_id = employee.emp_id WHERE appointment.emp_id = %s;"
            join_value = (empid,)           
            # query_join = f"SELECT appointment.start_time, patient.f_name, employee.f_name " \
            #                 f"FROM patient " \
            #                 f"INNER JOIN appointment ON patient.pat_id = appointment.pat_id " \
            #                 f"INNER JOIN employee ON appointment.emp_id = employee.emp_id " \
            #                 f"WHERE appointment.emp_id = '{empid}';"
            cur.execute(query_join, join_value)
            results  = cur.fetchall()
            
            top = tk.Toplevel()
            top.title("Patient Data")
            top.geometry("500x300")
            
            canvas = tk.Canvas(top)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar = tk.Scrollbar(top, command=canvas.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.configure(yscrollcommand=scrollbar.set)
            
            rec_frame = tk.Frame(canvas)
            canvas.create_window((0, 0), window=rec_frame, anchor='nw')
            
            
            column_names = [desc[0] for desc in cur.description]
            for i, name in enumerate(column_names):
                entry = tk.Entry(rec_frame)
                entry.insert(tk.END, name)
                entry.config(state='readonly', font=ArialTinyBold)
                entry.grid(row=0, column=i)

            for i, row in enumerate(results):
                for j, value in enumerate(row):
                    entry = tk.Entry(rec_frame)
                    entry.insert(tk.END, value)
                    entry.config(font=ArialTiny)
                    entry.grid(row=i+1, column=j)
                    
            def on_frame_configure(event):
                canvas.configure(scrollregion=canvas.bbox('all'))
            rec_frame.bind('<Configure>', on_frame_configure)
                
        except Exception as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
                
    query_button = tk.Button(appointment_frame, text="Your appointments", command=joinappointments)
    query_button.grid(row=9, column=1, pady=10, padx=10)

    appointment_frame.pack(pady=20, padx=20)


#This hides active page indicator
def hide_indicator():
    welcome_active.config(bg='#ABC7E3')
    patient_active.config(bg='#ABC7E3')
    presc_active.config(bg='#ABC7E3')
    qmedrec_active.config(bg='#ABC7E3')
    wmedrec_active.config(bg='#ABC7E3')
    umedrec_active.config(bg='#ABC7E3')
    login_active.config(bg='#ABC7E3')
    appointment_active.config(bg='#ABC7E3')

    
#Destroys old pages
def destroy_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()
    
    
#Active page indicator
def indicator(lb, page):
    hide_indicator()
    lb.config(bg='#5A5A5A')
    destroy_pages()
    page()
    
pages_frame = tk.Frame(root, bg='#ABC7E3')

buttonheight = 2
buttonwidth = 20
#Here are the buttons on the left side of the GUI
#Welcome button
welcome_button = tk.Button(pages_frame, text='Welcome', font=ArialTiny,
                           command=lambda: indicator(welcome_active, welcome_page),
                           width = buttonwidth, height = buttonheight)
welcome_button.pack(pady=12)

welcome_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
welcome_active.place(x=45, y=20, width=3, height=28)


#Add patient button
patient_button = tk.Button(pages_frame, text='Patients', font=ArialTiny,
                          command=lambda: indicator(patient_active, patient_page),
                          width = buttonwidth, height = buttonheight, state='disabled')
patient_button.pack(pady=12)

patient_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
patient_active.place(x=45, y=88, width=3, height=28)


#Write prescription button
presc_button = tk.Button(pages_frame, text='Write prescription', font=ArialTiny,
                         command=lambda: indicator(presc_active, presc_page),
                         width = buttonwidth, height = buttonheight, state='disabled')
presc_button.pack(pady=12)

presc_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
presc_active.place(x=45, y=156, width=3, height=28)


#Query medical records button
qmedrec_button = tk.Button(pages_frame, text='Medical records', font=ArialTiny,
                          command=lambda: indicator(qmedrec_active, qmedrec_page),
                          width = buttonwidth, height = buttonheight, state='disabled')
qmedrec_button.pack(pady=12)

qmedrec_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
qmedrec_active.place(x=45, y=224, width=3, height=28)


#Write a medical record button
wmedrec_button = tk.Button(pages_frame, text='Write a medical record', font=ArialTiny,
                          command=lambda: indicator(wmedrec_active, wmedrec_page),
                          width = buttonwidth, height = buttonheight, state='disabled')
wmedrec_button.pack(pady=12)

wmedrec_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
wmedrec_active.place(x=45, y=292, width=3, height=28)


#Update a medical record
umedrec_button = tk.Button(pages_frame, text='Update medical record', font=ArialTiny,
                          command=lambda: indicator(umedrec_active, umedrec_page),
                          width = buttonwidth, height = buttonheight, state='disabled')
umedrec_button.pack(pady=12)

umedrec_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
umedrec_active.place(x=45, y=360, width=3, height=28)

#Login button
login_button = tk.Button(pages_frame, text='Login', font=ArialTiny,
                          command=lambda: indicator(login_active, login_page),
                          width = buttonwidth, height = buttonheight)
login_button.pack(pady=12)

login_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
login_active.place(x=45, y=428, width=3, height=28)

#Appointments button
appointment_button = tk.Button(pages_frame, text='Appointment', font=ArialTiny,
                          command=lambda: indicator(appointment_active, appointment_page),
                          width = buttonwidth, height = buttonheight, state='disabled')
appointment_button.pack(pady=12)

appointment_active = tk.Label(pages_frame, text='', bg='#ABC7E3')
appointment_active.place(x=45, y=496, width=3, height=28)


# def login_button_status(*args):
#     if verify_login.verified == False:
#         patient_button.config(state='normal')
#         presc_button.config(state='normal')
#         qmedrec_button.config(state='normal')
#         wmedrec_button.config(state='normal')
#         umedrec_button.config(state='normal')
#         appointment_button.config(state='normal')
#         print(verify_login)

  
###### LOGIN TAB ######

def login_page():
    login_frame = tk.Frame(main_frame, bg=LightBlue)

    lb = tk.Label(login_frame, text="Employee login", font=ArialBig, bg=LightBlue)
    lb.grid(row=0, column=1) 

    username_label = tk.Label(login_frame, text="Username:", font=ArialSmall, bg=LightBlue)
    username_label.grid(row=1, column=0, pady=10, padx=10)

    username_entry = tk.Entry(login_frame, font=ArialSmall)
    username_entry.grid(row=1, column=1, pady=10, padx=10)

    passwd_label = tk.Label(login_frame, text="Password:", font=ArialSmall, bg=LightBlue)
    passwd_label.grid(row=2, column=0, pady=10, padx=10)

    passwd_entry = tk.Entry(login_frame, font=ArialSmall)
    passwd_entry.grid(row=2, column=1, pady=10, padx=10)
    
    login_submit_button = tk.Button(login_frame, text="Login", command=lambda: submit_login(username_entry, passwd_entry))
    login_submit_button.grid(row=3, column=1, pady=10, padx=10)
    print(LOGGED_IN, "Logged in global variable")
    
    login_frame.pack(pady=20, padx=20)

    ###### LOGIN BUTTON ######
def submit_login(username_entry, passwd_entry):
    user = username_entry.get()
    passwd = passwd_entry.get()
    
    verified = verify_login(user, passwd)
    print(verified, "is verified")
    
    global LOGGED_IN
    LOGGED_IN = verified

    #This clears the entries
    username_entry.delete(0, tk.END)
    passwd_entry.delete(0, tk.END)
    
    print(LOGGED_IN)
    if LOGGED_IN:
        patient_button.config(state='normal')
        presc_button.config(state='normal')
        qmedrec_button.config(state='normal')
        wmedrec_button.config(state='normal')
        umedrec_button.config(state='normal')
        appointment_button.config(state='normal')

###### LOGIN TAB ######

#The frames itself
pages_frame.pack(side=tk.LEFT, fill=tk.Y)
pages_frame.pack_propagate(False)
pages_frame.configure(width = 280)

main_frame = tk.Frame(root, bg=LightBlue)

main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
main_frame.pack_propagate(False)
root.mainloop()
