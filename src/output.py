import csv
from colorama import Fore, Back
from config import login_credentials_filename, cr, field_names
from cryptor import decrypt_user_credentials

def output_login_credentials():
    """Show saved credentials"""
    try:
        with open(login_credentials_filename) as csv_object:
            plain_credentials = csv.DictReader(csv_object)
            print(' -- '.join(field_names))
            for line in plain_credentials:
                title = line['Title']
                website = line['Website']
                username = line['Username']
                password = line['Password']
                password = decrypt_user_credentials(password)
                final_credentials = '{} {} {} {}'.format(title,website,
                username,Fore.LIGHTMAGENTA_EX+Back.LIGHTYELLOW_EX+password+cr)

                print(f'\n{final_credentials}')
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX +'\nNo login credentials were found!\n'+cr)
        pass