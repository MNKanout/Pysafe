# Builtin modules
import random
import string
from sys import platform
from getpass import getpass
# Dependencies
from colorama import Fore, init
# Local modules
from cryptor import encrypt_credentials
from config import cr

init()

def generate_password():
    """Generate password with a given length"""
    while True:
        length = input('Password length:')
        try:
            length = int(length)
        except ValueError:
            print(Fore.LIGHTRED_EX+"You didn't enter a number"+cr)
            continue
        else:
            custom_punctuation = "!#$%*+-?@_"
            password_mix = string.ascii_letters+string.digits+custom_punctuation
            p = []
            i = 0
            while i <= length:
                p.append(random.choice(password_mix))
                i = i + 1
            separator =''
            print(f'\nNew password:'
                  f'{Fore.LIGHTYELLOW_EX+(separator.join(p))}\n'+cr)
            while True:
                print('Regenerate password?(y/n)')
                regenerate = input()
                if regenerate.lower() == 'y':
                    break
                elif regenerate.lower() == 'n':
                    return (separator.join(p))
                else:
                    print(Fore.LIGHTRED_EX + "Enter a valid option!"+cr)
                    continue

def input_password():
    """Accept password from user"""
    while True:
        gen_password = input('Generate password / Save password?(g/s):')
        if gen_password.lower() == 'g':
            plain_password = generate_password()
            password = encrypt_credentials(plain_password)
            return password
        elif gen_password.lower() == 's':
            if platform == 'win32':
                print(Fore.LIGHTRED_EX+'Mouse right-click to paste '
                                       'passwords!'+cr)
            else:
                plain_password = getpass('New password:')
                password = encrypt_credentials(plain_password)
                return password
        else:
            print(Fore.LIGHTRED_EX+'Enter a valid option!'+cr)
            continue

