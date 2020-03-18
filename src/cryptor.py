# Dependencies
from colorama import Fore, init
from cryptography.fernet import Fernet
# Local modules
from keys import get_key, generate_key, enter_key
from config import cr

init()

def encrypt_credentials(password):
    """Encrypt credentials using the provided key"""
    try:
        key = get_key()
        f_1 = Fernet(key)
        token = f_1.encrypt(password.encode())
        token = token.decode()
        return token

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX+'No encryption key was found!\n'+cr)

        while True:
            user_choice = input('(Generate key)(Input key)(cancel)?(g)(i)(c)')
            if user_choice.lower() == 'c':
                print(Fore.LIGHTRED_EX+'You need an encryption key to '
                    'encrypt your login credentials!\nBack to the main '
                                       'menu!\n'+cr)
                break

            elif user_choice.lower() == 'g':
                key = generate_key()
                f_1 = Fernet(key)
                token = f_1.encrypt(password.encode())
                token = token.decode()
                return token

            elif user_choice.lower()=='i':
                key = enter_key()
                f_1 = Fernet(key)
                token = f_1.encrypt(password.encode())
                token = token.decode()
                return token
            else:
                print(Fore.LIGHTRED_EX+'Please enter a valid option!'+cr)
                continue




def decrypt_user_credentials(token):
    """Decrypt saved credentials"""
    try:
        key = get_key()
        f_1 = Fernet(key)
        token = bytes(token,'utf-8')
        password = f_1.decrypt(token)
        password = password.decode()
        return password

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX+'No encryption key was found')
        while True:
            user_choice = input('Enter encryption key?(y/n)')
            if user_choice.lower() == 'y':
                key = enter_key()
                f_1 = Fernet(key)
                token = bytes(token,'utf-8')
                password = f_1.decrypt(token)
                password = password.decode()
                return password
