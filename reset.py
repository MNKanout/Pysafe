import os
from colorama import Fore,Back
from keys import key_path
from input import login_credentials

def delete_all():
    """Delete credentials and keys"""
    confirm = input("Delete saved encryption key and login credentials?(y/n)\t")
    if confirm.lower() == 'y':
        try:
            os.remove(key_path)
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX +'\nNo encryption key was found\n')
        else:
            print(Fore.BLACK + Back.GREEN +'\nEncryption key has been deleted')
        try:
            os.remove(login_credentials)
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX +'\nNo login credentials were found\n')
        else:
            print(Fore.BLACK + Back.GREEN +'\nAll login Credentials have been'
                                           ' deleted!\n')


    elif confirm.lower() =='n':
        print('\n\u001b[31mNo key nor login credentials got deleted\u001b[0m')
        pass

    else:
        print('\n\u001b[31mNo valid option got selected, back to the main '
              'menu!\u001b[0m\n')
        pass