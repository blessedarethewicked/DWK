import sys
import os
import hashlib
import csv


commands = ['-u', '-p','-n','-r']

def add_new_user(username,password,role):
    """
    this function adds a new user. it requires a username and password
    example:
    python login -n [username] -p [password]
    """
    print('\n Adding a new user ')

    # genarate the hashed password 
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    print(hashed_password)
    user = [username,hashed_password,role]

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

    with open("user_password.csv","r") as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row =='[]':continue
            # if the user exits we check the password
            if username in row:
                hashed_password= hashlib.sha256(password.encode()).hexdigest()
                if hashed_password== row[1]:
                    print(' the Password matches')
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
    elif arguments[1]== '-u':
        login(arguments[2],arguments[4])
    else:
        return

# this checks if the argments in argv are valid
for i in range(1,len(sys.argv)):
    # checks if the current argment is a flag and if its not we move on to the next
    if (i % 2)==0:continue
    if sys.argv[i] in commands: continue
    else: 
        print(f'{sys.argv[i]} is not a valid command')
        print(commands, ' theses are the valid commands')
        quit()


call_function(sys.argv)
print(' \ntest passed: exiting script')
