import csv
from colorama import Fore, Back, init
from config import login_credentials_filename, cr
from cryptor import decrypt_user_credentials

init()

def output_login_credentials():
    """Show saved credentials"""
    try:
        with open(login_credentials_filename) as f:
            csv_reader = csv.DictReader(f)
            field_names = '\t{:<20} {:<20} {:<20} {:<20}'.format(
                'Title','Website','Username','Password')
            i = 0
            print(Fore.BLACK+Back.WHITE+field_names+cr)
            for line in csv_reader:
                i = i + 1
                title = line['Title']
                website = line['Website']
                username = line['Username']
                password = line['Password']
                password = decrypt_user_credentials(password)
                final_ = '{:<20} {:<20} {:<20} {:<20}'.format(title,website,
                                                            username,password)

                print(f'\n{Fore.WHITE+Back.BLACK+str(i)}.\t{final_+cr}')
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX+'\nNo login credentials were found!\n'+cr)
        pass