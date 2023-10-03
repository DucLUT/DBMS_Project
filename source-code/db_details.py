import json
# Test constants for db connection. Comment out the one 
# you are not using.
with open('connection_config.json', 'r') as file:
    config = json.load(file)
    
HOST = config['HOST']
DATABASE = config['DATABASE']
USER = config['USER']
PASSWORD = config['PASSWORD']
PORT = config['PORT']

# Constants for minimum length of user login details.
MIN_USER_LEN = 8
MIN_PASSWD_LEN = 8

# Constants for maximum length of user login details.
MAX_USER_LEN = 255
MAX_PASSWD_LEN = 255
