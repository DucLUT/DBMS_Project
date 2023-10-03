# pip install argon2-cffi
import argon2
import psycopg2
import db_details

# NOTE: Only use create_user and verify_login outside of 
# this module! The rest are internal functions.

def check_inputs(user, passwd):

    # If the minimum length is not met or the input is not valid 
    # utf-8, return false, else return true. 
    for char in user:
        if char.isspace():
            return (False, "NoSpaceError")
    for char in passwd:
        if char.isspace():
            return (False, "NoSpaceError")
    
    if (len(user) >= db_details.MIN_USER_LEN) and (len(passwd) >= db_details.MIN_PASSWD_LEN):
        try:
            user.encode('utf-8')
            passwd.encode('utf-8')
            return (True, "OK")
        except UnicodeError:
            return (False, "InvalidCharError")
    else:
        return (False, "InvalidLengthError")


def get_user(user):

    try:
        with psycopg2.connect(
            host = db_details.HOST,
            database = db_details.DATABASE,
            user = db_details.USER,
            password = db_details.PASSWORD,
            port = db_details.PORT,
            ) as conn:
            
            with conn.cursor() as cur:
                get_command = "SELECT email, passwd FROM users WHERE email = %s"
                get_values = (user,)
                
                cur.execute(get_command, get_values)
                records = cur.fetchall()
                
                return records
                
    except Exception as e:
        print("ERROR:",e)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

# Only use this and verify_login outside of this module
def create_user(user, passwd):
    
    val_inputs = check_inputs(user, passwd)
    if not val_inputs[0]:
        return False
    
    hasher = argon2.PasswordHasher()
    passhash = hasher.hash(passwd)
    
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
                insert_command = "INSERT INTO users(username, passwd) VALUES (%s, %s);"
                insert_values = (user, passhash)
                cur.execute(insert_command, insert_values)
                print(passhash)
                print("success")
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


def validate_password(passwd, user_details):
    
    passhash = user_details[0][1]
    hasher = argon2.PasswordHasher()
    verified = hasher.verify(passhash, passwd)
    
    return verified

# Only use this and create_user outside of this module
def verify_login(user, passwd):
    
    # Get username and password hash if they exist, if they
    # don't exist, return empty list, else return list with one
    # tuple: (username, passwd)
    user_details = get_user(user)
    
    # If they don't exist, return false
    if len(user_details) == 0:
        return False
    
    # Check if the password is valid and return the result
    valid_passwd = validate_password(passwd, user_details)
    return valid_passwd

