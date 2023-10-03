# database-systems-project

## Welcome
!!! IMPORTANT !!!
When starting the program you need to first go to the welcome page and insert 
the database password for user postgres. It will display whether the 
connection was successful or not.

## Important information about input fields and start-up

Please make sure to check the format of the data entered in the input fields, 
so that it matches the desired format. And make sure there are no extra 
whitespace characters where they are not wanted, as they can alter the 
results. 

If you are unable to connect to the database, make sure that the database 
connection information in the connection_config.json file is correct. 
That file contains information such as database name, host name, password, user & port. Sometimes the password for the database may be different between 
computers. 

Our default password in the json config file is: postgres

To edit the json config file you can open it in for example notepad or vscode 
etc. Make sure you're careful when changing the details in that file. 

''' mQHiLhyE5@h728CEcD

## Logging in
All menu buttons except for login and welcome will be disabled until a 
successful login.

You can find a list of employee login details in the "user_accounts.txt" 
file. The file contains the email (username) and plaintext password of each 
employee id.

'''The format is: <emp_id>) <email/username>: <password>

When copying and pasting the email/usernames and passwords into their 
respective login fields, make sure to check that there are no spaces or tabs, 
and that the email/usernames and passwords perfectly match those in the 
"user_accounts.txt" file. 

As an example, if you want to login with the account,
"john.doe@lahti.hospital.fi" then you need to insert into the login fields 
the following,

Username: john.doe@lahti.hospital.fi
Password: myfavoritefood_myfavoritecolor

## Querying, inserting and deleting patients

### Querying patients
You can either query all patients in the database or you can query patients 
by their last name. To query all patients you should leave the "You can query 
patients by last name. Else leave the field empty." field empty (make sure 
that it is completely empty, e.g. no spaces, tabs etc.). Else write in the 
last name of the patient you want to search for (only one patient!), again 
make sure there are no extra empty characters, spaces and tabs etc. 

The query will open in a pop up window that will list all of the searched 
patients and their information. 

### Inserting patients
To insert patients you should add fill in the fields under the label "Add a 
patient" and make sure that the filled in information is in the correct 
format. 

First name and last name should each at most be 255 characters long, age 
should be a small integer from 0 to not much more than say 120. 

Gender should only be a single character, either M or F. M for male, F for 
female.

Address should be at most 255 characters long. 

The phone number should contain the international calling codes, example: +358
and they should not be longer than 50 characters. 

The SSN, social security number, should be a at most 20 characters long, 
unique alphanumerical string. 

For all insertions, make sure there are no spaces, tabs or other such 
whitespace characters.

Once done, press "Submit".

### Deleting patients
To delete patients you should insert the patient id (pat_id) of the patient 
who you wish to delete from the database. When doing so you will delete the 
patient along with all their records, appointments and other information. 

If you wish to confirm the details of the patient who you are deleting first, 
then you should query them either by last name or query all patients and find 
the one you wish to delete. 

Again make sure the field doesn't contain any extra whitespace characters. 

## Querying, writing and updating medical records

### Querying records
To query medical records you should click on the "Medical records" button on 
the left side and then to query all patients you need to check the "Select 
all patients" box and press "Query patient". And to query the records of an 
individual patient you need to insert the patient's id in the entry box under 
the lable "Patient's ID" and make sure that the "Select all patients" 
checkbox is NOT checked and then press "Query patient". 

### Writing records
To write a medical record, press the "Write a medical record" button on the 
left and then insert the information of the record into their relative 
fields. You should insert the employee id of that employee who you are logged 
in as, the patient id of an existing patient, optional symptoms, optional 
diagnosis (as an ICD-11 standard diagnosis code), optional procedures as a 
longer text block e.g. "This patient has undergone several procedures, 
including a knee surgery and physical therapy related to said surgery.", and 
same for notes (longer text block). To write a prescription for the medical 
record, see the section "Writing prescriptions" in this file. 

### Updating records
To update a medical record, insert the record id into the input field under 
the label "Insert record ID:", you can query the medical records, explained 
in the section "Querying records" to find out the record ids of the records 
you wish to update. When updating check ONLY ONE of the checkboxes of the 
attribute that you wish to update/change. One you have made sure that only 
one of the boxes is checked, write the desired information in the input field 
below, under the label "Update text" and finally press "Submit".

### Writing prescriptions
To write a prescription for a medical record press "Write prescription" on 
the left in the menu and insert the record id, the instructions for the 
prescription and the medication contained in the prescription into their 
respective fields, and finally press "Submit".

## Scheduling and querying appointments
To schedule and query appointments press "Appointment" on the left in the 
menu and insert the asked for information into the fields under the label 
"Schedule appointment" if you wish to schedule an appointment and finally 
press "Schedule". To see your own appointments/the appointments of a specific 
employee, insert the employee id into the input field under the label "To see 
your own appointments, enter your Emp IP and press "Your appointments"", 
finally press "Your appointments".

## About formats for diagnosis ids and medications ids
The diagnosis and medication ids should be written in the ICD-11 standard 
format. 

