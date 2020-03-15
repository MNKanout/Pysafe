import csv
import pathlib
from colorama import Fore, Back
from password import input_password

cr = Fore.RESET + Back.RESET # Short for color rest
login_credentials_filename = str(pathlib.Path('login_credentials.csv').absolute())
field_names = ['title','website','username','password']

def input_login_credentials():
    """Accept user input"""
    title = input('Website title:')
    website = input('Website link:')
    username = input('Username/email:')
    password = input_password()
    save_user_input(title, website, username, password)

def save_user_input(title,website,username,password):
    """Save credentials to a CSV file"""
    try:
        if open(login_credentials_filename):#Append to file a login credentials file
            with open(login_credentials_filename,'a+',newline='') as f:
                thewriter = csv.DictWriter(f,fieldnames=field_names)
                thewriter.writerow({'title':title,'website':website,'username':
                                                username,'password':password})
                print(f"Login credentials has been Saved to"
                      f"{Fore.LIGHTYELLOW_EX}"
                        f"{login_credentials_filename+ cr}\n")

    except FileNotFoundError:#Create a new login credentials file
        with open(login_credentials_filename,'w+',newline='') as f:
            thewriter = csv.DictWriter(f,fieldnames=field_names)
            thewriter.writeheader()
            thewriter.writerow({'title':title,'website': website,'username':
                                             username,'password': password})
            print(f"Login credentials has been Saved to"
                  f"{Fore.LIGHTYELLOW_EX}"
                    f"{login_credentials_filename+cr}\n")

