import random
import string


def generate_password():
    """Generate password based with a given length"""
    while True:
        length = input('Number of the password characters:')
        try:
            length = int(length)
        except ValueError:
            print("\u001b[31mYou didn't enter a number\u001b[0m")
            continue
        else:
            custom_punctuation = "!#$%*+-?@_"
            password_mix = string.ascii_letters + string.digits + custom_punctuation
            p = []
            i = 0
            while i <= length:
                p.append(random.choice(password_mix))
                i = i + 1
            s = ''
            print(f'\nNew password:\u001b[33m{s.join(p)}\u001b[0m\n')
            return (s.join(p))



