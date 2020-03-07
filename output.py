import csv
from input import login_credentials
from crypt import decrypt_user_credentials

def show_saved_logins():
    """Show saved credentials"""
    try:
        with open(login_credentials) as csv_object:
            plain_credentials = csv.DictReader(csv_object)
            for line in plain_credentials:
                title = line['title']
                website = line['website']
                username = line['username']
                token = line['password']
                token = bytes(token[1:], 'utf-8')
                password = decrypt_user_credentials(token)
                password = str(password)
                password = password[1:]
                final_credentilas = '{} {} {} {}'.format(title,website,username,
                                                         password)
                print(f'\n\u001b[33m{final_credentilas}\u001b[0m\n')
    except FileNotFoundError:
        print(f'\n\u001b[31mNo credentilas were found!\u001b[0m\n')
        pass

