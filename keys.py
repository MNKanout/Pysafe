from cryptography.fernet import Fernet
key_path = 'key.txt'

def generate_new_key():
    """Generate a new encryption key"""
    key = Fernet.generate_key()
    print(f'\nEncryption key:\t\u001b[33m{key}\u001b[0m\n')
    save_key_to_file(key)


def save_key_to_file(key):
    """Save generated key to file"""
    while True:
        save_file = input("\u001b[31mSave key to file? This will erase any "
                          "existed key!\u001b[0m"
                                                                   "(y/n)\t")
        if save_file.lower() == 'y':
            with open(key_path,'wb') as key_object:
                key_object.write(key)
                print(f'\n\u001b[31mThe encryption key has been saved '
                      f'to\u001b[0m {key_path}\n')
                break

        elif save_file.lower() == 'n':
            break

        else:
            print('\n\u001b[31mPlease enter a valid option!\u001b[0m\n')
            continue

def get_key():
    """Use a saved key file"""
    with open(key_path,'rb') as key_object:
        key = key_object.read()
        return key
