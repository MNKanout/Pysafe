import csv
from colorama import Fore
from config import login_credentials_filename, field_names, cr
from password import input_password


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
        if open(login_credentials_filename):#Append to file
            with open(login_credentials_filename,'a+',newline='') as f:
                thewriter = csv.DictWriter(f,fieldnames=field_names)
                thewriter.writerow({'title':title,'website':website,'username':
                                                username,'password':password})
                print(f"Login credentials has been Saved to"
                      f"{Fore.LIGHTYELLOW_EX}"
                        f"{login_credentials_filename+ cr}\n")

    except FileNotFoundError:   #Create new file.
        with open(login_credentials_filename,'w+',newline='') as f:
            thewriter = csv.DictWriter(f,fieldnames=field_names)
            thewriter.writeheader()
            thewriter.writerow({'title':title,'website': website,'username':
                                             username,'password': password})
            print(f"Login credentials has been Saved to"
                  f"{Fore.LIGHTYELLOW_EX}"
                    f"{login_credentials_filename+cr}\n")

