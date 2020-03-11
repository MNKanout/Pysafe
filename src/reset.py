import os
from colorama import Fore,Back
from keys import key_path
from input import login_credentials

cr = Fore.RESET + Back.RESET

def delete_all():
    """Delete credentials and keys"""
    confirm = input("Delete saved encryption key and login credentials?(y/n)\t")
    if confirm.lower() == 'y':
        try:
            os.remove(key_path)
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX +'No encryption key was found\n'+cr)
        else:
            print(Fore.BLACK+Back.GREEN +'Encryption key has been '
                                         'deleted!'+cr+'\n')
        try:
            os.remove(login_credentials)
        except FileNotFoundError:
            print(Fore.LIGHTRED_EX +'No login credentials were found'+cr+'\n')
        else:
            print(Fore.BLACK + Back.GREEN +'All login Credentials have been'
                                           ' deleted!'+cr+'\n')


    elif confirm.lower() =='n':
        print(Fore.BLACK+Back.GREEN+'No key nor login credentials got '
                                    'deleted'+cr+'\n')
        pass

    else:
        print(Fore.LIGHTRED_EX +'No valid option got selected, back to the '
                                'main menu!'+cr+'\n')
        pass