from colorama import Fore
from cryptography.fernet import Fernet
from keys import get_key, generate_new_key


def encrypt_credentials(plain_password):
    """Encrypt credentials using the provided key"""
    try:
        key = get_key()
        f_1 = Fernet(key)
        token = f_1.encrypt(plain_password.encode())
        return token

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX +'No encryption key was found!')
        user_choice = input('Do you wish to generate a new one now?(y/n)')
        while True:
            if user_choice.lower() == 'n':
                print(Fore.LIGHTRED_EX+'You need an encryption key to '
                    'encrypt your login credentials!\nBack to the main menu!\n')
                break
            elif user_choice.lower() == 'y':
                generate_new_key()
                key = get_key()
                f_1 = Fernet(key)
                token = f_1.encrypt(plain_password.encode())
                return token

def decrypt_user_credentials(token):
    """Decrypt saved credentials"""
    key = get_key()
    f_1 = Fernet(key)
    password = f_1.decrypt(token)
    return password