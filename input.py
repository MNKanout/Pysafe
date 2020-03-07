import csv
import getpass
from crypt import encrypt_credentials
from password import generate_password

login_credentials = 'login_credentials.csv' #Login credentials file
field_names = ['title', 'website', 'username', 'password']

def accept_user_input():
    """save username, password, and website"""
    title = input('Website title:')
    website = input('Website link:')
    user_name = input('Username/email:')

    while True:
        gen_password = input('\u001b[31mGenerate password / Save password?('
                             'g/s):\u001b[0m')
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
            print('\u001b[31mEnter a valid option!\u001b[0m')
            continue




def save_user_input(title,website,username,password):
    """Save credentials into an CSV file"""
    try:
        if open(login_credentials):#Save new credentials without creating a new file
            with open(login_credentials,'a+',newline='') as f:
                thewriter = csv.DictWriter(f, fieldnames=field_names)
                thewriter.writerow({'title':title,'website':website,
                                    'username':username,'password':password})
                print('\n\u001b[31mCredentials have been saved\u001b[0m\n')

    except FileNotFoundError:#Create a new file for login credentials if no file
        # was found
        with open(login_credentials, 'w+', newline='') as f:
            thewriter = csv.DictWriter(f, fieldnames=field_names)
            thewriter.writeheader()
            thewriter.writerow({'title':title,'website': website,'username':
                username,'password': password})
            print('\n\u001b[31mSaving is complete\u001b[0m\n')

