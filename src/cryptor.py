from colorama import Fore
from cryptography.fernet import Fernet
from keys import get_key,generate_new_key,enter_key


def encrypt_credentials(plain_password):
    """Encrypt credentials using the provided key"""
    try:
        key = get_key()
        f_1 = Fernet(key)
        token = f_1.encrypt(plain_password.encode())
        return token

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX +'No encryption key was found!')
        user_choice = input('Generate/Enter encryption key? Or cancel('
                            'g/e/c)')
        while True:
            if user_choice.lower() == 'c':
                print(Fore.LIGHTRED_EX+'You need an encryption key to '
                    'encrypt your login credentials!\nBack to the main menu!\n')
                break

            elif user_choice.lower() == 'g':
                generate_new_key()
                key = get_key()
                f_1 = Fernet(key)
                token = f_1.encrypt(plain_password.encode())
                return token

            elif user_choice.lower()=='e':
                key = enter_key()
                f_1 = Fernet(key)
                token = f_1.encrypt(plain_password.encode())
                return token
            else:
                print(Fore.LIGHTRED_EX+'Please enter a valid option!')
                continue




def decrypt_user_credentials(token):
    """Decrypt saved credentials"""
    try:
        key = get_key()
        key = key.encode()
        f_1 = Fernet(key)
        password = f_1.decrypt(token)
        return password

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX+'No encryption key was found')
        while True:
            user_choice = input('Enter encryption key?(y/n)')
            if user_choice.lower() == 'y':
                key = enter_key()
                key = key.encode()
                f_1 = Fernet(key)
                password = f_1.decrypt(token)
                return password
