import csv
from sys import platform
import getpass
import pathlib
from colorama import Fore, Back
from cryptor import encrypt_credentials
from password import generate_password

cr = Fore.RESET + Back.RESET
login_credentials = 'login_credentials.csv' #Login credentials filename
login_credentials_absolute = str(pathlib.Path(login_credentials).absolute())
field_names = ['title', 'website', 'username', 'password']

def accept_user_input():
    """Accept user input"""
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
            if platform == 'win32':
                print(Fore.LIGHTRED_EX+'Mouse right-click to paste passwords!')
            else:
                plain_password = getpass.getpass('New password:')
                password = encrypt_credentials(plain_password)
                save_user_input(title,website,user_name,password)
                break
        else:
            print(Fore.LIGHTRED_EX +'Enter a valid option!'+cr)
            continue




def save_user_input(title,website,username,password):
    """Save credentials to a CSV file"""
    try:
        if open(login_credentials):    #Append to file a login credentials file
            with open(login_credentials,'a+',newline='') as f:
                thewriter = csv.DictWriter(f,fieldnames=field_names)
                thewriter.writerow({'title':title,'website':website,'username':
                                                username,'password':password})
                print(f"Login credentials has been Saved to"
                      f"{Fore.LIGHTYELLOW_EX}"
                        f"{login_credentials_absolute+cr}\n")

    except FileNotFoundError:   #Create a new login credentials file
        with open(login_credentials,'w+',newline='') as f:
            thewriter = csv.DictWriter(f,fieldnames=field_names)
            thewriter.writeheader()
            thewriter.writerow({'title':title,'website': website,'username':
                                             username,'password': password})
            print(f"Login credentials has been Saved to"
                  f"{Fore.LIGHTYELLOW_EX}"
                    f"{login_credentials_absolute+cr}\n")

