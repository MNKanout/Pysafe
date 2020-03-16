import csv
from colorama import Fore,Back
from input import login_credentials_filename
from keys import key_filename
from cryptor import decrypt_user_credentials

def output_login_credentials():
    """Show saved credentials"""
    try:
        with open(login_credentials_filename) as csv_object:
            plain_credentials = csv.DictReader(csv_object)
            for line in plain_credentials:
                title = line['title']
                website = line['website']
                username = line['username']
                password = line['password']
                password = decrypt_user_credentials(password)
                final_credentials = '{} {} {} {}'.format(title,website,username,
                            Fore.LIGHTMAGENTA_EX+Back.LIGHTYELLOW_EX+password)
                print(f'\n{final_credentials}')
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX +'\nNo credentials were found!\n')
        pass

def output_path():
    """Show absolute path to saved key file and login credentials file """
    print(f'Encryption key file path: {key_filename}')
    print(f'Login credentials file path: {login_credentials_filename}')


