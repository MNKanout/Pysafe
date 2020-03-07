import os
from keys import key_path
from input import login_credentials

def delete_all():
    """Delete credentials and keys"""
    confirm = input("\u001b[31mDelete saved encryption key and login "
                    "credentials?'y/n'\u001b[0m\t")
    if confirm.lower() == 'y':
        try:
            os.remove(key_path)
        except FileNotFoundError:
            print('\n\u001b[31mNo encryption key was found\n Searching for '
                  'login credentials...\u001b[0m')
        else:
            print('\n\u001b[31mEncryption key has been deleted\u001b[0m')
        try:
            os.remove(login_credentials)
        except FileNotFoundError:
            print('\n\u001b[31mNo login credentials were found\u001b[0m\n')
        else:
            print('\n\u001b[31mAll login Credentials have been deleted!\u001b['
                  '0m\n')


    elif confirm.lower() =='n':
        print('\n\u001b[31mNo key nor login credentials got deleted\u001b[0m')
        pass

    else:
        print('\n\u001b[31mNo valid option got selected, back to the main '
              'menu!\u001b[0m\n')
        pass