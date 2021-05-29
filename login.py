import sys
import hashlib
import csv
import re
import hashlib, uuid


commands = ['-u', '-p','-n','-r']

def print_conditions():
    """
     this function prints the conditions for the user and password strings
    """

    print('Username conditions: \n')

    print(' Must be 8-15 characters and must start with a letter')
    print(' May not contain special characters – only letters and numbers \n')

    print('password conditions:\n')
    print(' Must be 5-20 characters long')
    print(' Must contain at least one lower-case letter (abcdefghijklmnopqrstuvwxyz)')
    print(' Must contain at least one number (0123456789)')
    print(' Must not contain a colon (:); an ampersand (&); a period (.); a tilde (~); or a space.')
    return 0 

def add_new_user(username,password,role):
    """
    this function adds a new user. it requires a username and password
    example:
    python login -n [username] -p [password]
    """
    print('\n Adding a new user ')

    # checking conditions for the password
    if re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]{7,15}', username):
        print('the username given is valid')
    else:
        print('the username given is not valid')
        return 0
    if re.fullmatch(r'[^: \&\.\~]*[a-z0-9]+[^:\&\.\~]{5,20}', password):
        print('the password given is valid')
    else:
        print('the password given is not valid')
        return 0


    # genarate salt and then hash 
    salt = uuid.uuid4().hex
    key = salt + password
    print(salt)
    hashed_password= hashlib.sha256(key.encode()).hexdigest()
    print(hashed_password)
    user = [username,salt,hashed_password,role]

    # check if we have already saves that user
    print('checking if user alredy exits')
    with open("user_password.csv","r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row =='[]':continue
            # if the user already exits then we leave this loop
            if username in row:
                print(f'user {username} already exits ')
                return 0

    # save this to the csv file 
    with open("user_password.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow(user)
        

    return 0

def login(username,password):
    """
    this function adds a new user. it requires a username and password
    example:
    python login -u [username] -p [password]
    """
    print('\nfuntion login')

    # checking conditions for the password
    if re.fullmatch(r'[a-zA-Z][a-zA-Z0-9]{7,15}', username):
        print('the username given is valid')
    else:
        print('the username given is not valid')
        return 0
    if re.fullmatch(r'[^: \&\.\~]*[a-z0-9]+[^:\&\.\~]{5,20}', password):
        print('the password given is valid')
    else:
        print('the password given is not valid')
        return 0



    with open("user_password.csv","r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row =='[]':continue
            # if the user exits we check the password
            if username in row:
                print(row[1])
                key = row[1] + password
                hashed_password= hashlib.sha256(key.encode()).hexdigest()
                print(hashed_password)
                if hashed_password== row[2]:
                    print('the Password matches')
                else:
                    print('wrong password')
                return 0

    return 0

def call_function(arguments):
    """
    This functions job is to tall the correct function based on the argv inputs
    """
    if arguments[1]== '-n':
        add_new_user(arguments[2],arguments[4],arguments[6])
        return 0
    elif arguments[1]== '-u':
        login(arguments[2],arguments[4])
        return 0 
    else:
        return 0

# this checks if the argments in argv are valid
for i in range(1,len(sys.argv)):
    # checks if the current argment is a flag and if its not we move on to the next
    if (i % 2)==0:continue
    if sys.argv[i] in commands: continue
    else: 
        print(f'{sys.argv[i]} is not a valid command')
        print(commands, ' theses are the valid commands')
        quit()




print_conditions()
if call_function(sys.argv)==0:
    print('exited with an error')
else:
    print(' \ntest passed: exiting script')
