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
        user_choice = input('\n\u001b[31mNo encryption key was found, do you '
                            'wish to generate a new one now?(y/n)\u001b[0m\n')
        while True:
            if user_choice.lower() == 'n':
                print('\u001b[31mYou need an encryption key to encrypt your '
                      'login credentials! back to the main menu!\u001b[0m\n')
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