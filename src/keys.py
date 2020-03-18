import json
from colorama import Fore, init
from cryptography.fernet import Fernet
from config import key_filename, cr

init()

def generate_key():
    """Generate a new encryption key"""
    while True:
        print(f'Are you sure you want to generate a new encryption key? '
        f'{Fore.LIGHTRED_EX}This will erase any existed encryption key?{cr}'
        f'(y/n)')
        user_choice = input()
        if user_choice.lower() == 'y':
            key = Fernet.generate_key()
            key = key.decode()
            print(f'\nEncryption key:{Fore.LIGHTYELLOW_EX+(key)}\n'+cr)
            save_key_to_file(key)
            return key
        elif user_choice.lower() == 'n':
            break
        else:
            print('Please enter a enter a valid option!')
            continue

def save_key_to_file(key):
    """Save generated key to file"""
    with open(key_filename,'w') as f:
        json.dump(key, f,)
        #f.write(key)
        print(f"\nThe encryption key has been saved to" +
              f"{Fore.LIGHTYELLOW_EX+key_filename}"+cr)

def get_key():
    """Read key from file"""
    with open(key_filename, 'r') as key_object:
        key = json.load(key_object)
        key = key.encode()
        return key

def enter_key():
    """Input key from user"""
    key = input('Enter encryption key:')
    if len(key) == 46 and key[44] == '=':
        save_key_to_file(key)
        key = key.encode()
        return key
    else:
        print(Fore.LIGHTRED_EX+'\nYou entered an invalid key!')

