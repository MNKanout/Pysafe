import pathlib
from colorama import Fore, Back

login_credentials_filename = str(pathlib.Path('login_credentials.csv').absolute())
key_filename = str(pathlib.Path('key.json').absolute())
cr = Fore.RESET + Back.RESET
field_names = ['Title','Website','Username','Password']
