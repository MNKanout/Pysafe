import csv
import getpass
from colorama import Fore, Back
from cryptor import encrypt_credentials
from password import generate_password

cr = Fore.RESET + Back.RESET
login_credentials = 'login_credentials.csv' #Login credentials file
field_names = ['title', 'website', 'username', 'password']

def accept_user_input():
    """save username, password, and website"""
    title = input('Website title:')
    website = input('Website link:')
    user_name = input('Username/email:')

    while True:
        gen_password = input('Generate password / Save password?(g/s):')
        if gen_password.lower() == 'g':
            plain_password = generate_password()
            password = encrypt_credentials(plain_password)
            save_user_input(title,website,user_name,password)
            break

        elif gen_password.lower() == 's':
            plain_password = getpass.getpass('New password:')
            password = encrypt_credentials(plain_password)
            save_user_input(title,website,user_name,password)
            break

        else:
            print(Fore.LIGHTRED_EX +'Enter a valid option!'+cr)
            continue




def save_user_input(title,website,username,password):
    """Save credentials into an CSV file"""
    try:
        if open(login_credentials):#Append to file
            with open(login_credentials,'a+',newline='') as f:
                thewriter = csv.DictWriter(f, fieldnames=field_names)
                thewriter.writerow({'title':title,'website':website,
                                    'username':username,'password':password})
                print(Fore.BLACK + Back.LIGHTGREEN_EX +'Saving is '
                                                       'complete'+cr+'\n')

    except FileNotFoundError:#Create a new file
        with open(login_credentials, 'w+', newline='') as f:
            thewriter = csv.DictWriter(f, fieldnames=field_names)
            thewriter.writeheader()
            thewriter.writerow({'title':title,'website': website,'username':
                username,'password': password})
            print(Fore.BLACK + Back.LIGHTGREEN_EX +'\nSaving is '
                                                   'complete'+cr+'\n')

