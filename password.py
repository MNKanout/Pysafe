import random
import string
from colorama import Fore


def generate_password():
    """Generate password based with a given length"""
    while True:
        length = input('Number of the password characters:')
        try:
            length = int(length)
        except ValueError:
            print(Fore.LIGHTGREEN_EX+"You didn't enter a number")
            continue
        else:
            custom_punctuation = "!#$%*+-?@_"
            password_mix = string.ascii_letters + string.digits\
                           + custom_punctuation
            p = []
            i = 0
            while i <= length:
                p.append(random.choice(password_mix))
                i = i + 1
            separator = ''
            print(f'\nNew password:{Fore.LIGHTYELLOW_EX + separator.join(p)}\n')
            while True:
                print(Fore.LIGHTRED_EX + 'Regenerate password?(y/n)')
                regenerate = input()
                if regenerate.lower() == 'y':
                    break
                elif regenerate.lower() == 'n':
                    return (separator.join(p))
                else:
                    print(Fore.LIGHTRED_EX + "Enter a valid option!")
                    continue


