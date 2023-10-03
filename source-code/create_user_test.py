import psycopg2
import argon2
import db_details

def create_user_test():
    
    hasher = argon2.PasswordHasher()
    
    try:
        with psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            ) as conn:
            
            with conn.cursor() as cur:
                # Add to improvement part of document, SQL Injection protection
                # by using prepared statements.
                for i in range(1,9):
                    passwd = str(input("Enter password for emp_id ({}): ".format(i)))
                    passhash = hasher.hash(passwd)
                    
                    insert_command = "INSERT INTO users VALUES ({}, (SELECT email FROM employee WHERE emp_id = {}), '{}');".format(i, i, passhash)
                    email_command = "SELECT email FROM employee WHERE emp_id = {}".format(i)
                    
                    cur.execute(insert_command)
                    print(passhash)
                    print("success")
                    
                    cur.execute(email_command)
                    record = cur.fetchall()
                    with open("user_accounts.txt", "a") as f:
                        f.write(f"{i}) {record}: {passwd}")
                        
                    char_count = 0
                    for char in passhash:
                        char_count += 1
                    print("passhash length:",char_count)
                
    except Exception as e:
        print("ERROR:",e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()