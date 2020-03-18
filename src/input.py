import csv
from colorama import Fore, Back, init
from config import login_credentials_filename, field_names, cr
from password import input_password

init()

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
        if open(login_credentials_filename):#Append to file without header
            with open(login_credentials_filename,'a+',newline='') as f:
                thewriter = csv.DictWriter(f,fieldnames=field_names)
                thewriter.writerow({'Title':title,'Website':website,'Username':
                                                username,'Password':password})
                print(f"{Fore.BLACK+Back.GREEN}Saving was successful"+cr)

    except FileNotFoundError:   #Create new file with header
        with open(login_credentials_filename,'w+',newline='') as f:
            thewriter = csv.DictWriter(f,fieldnames=field_names)
            thewriter.writeheader()
            thewriter.writerow({'Title':title,'Website': website,'Username':
                                             username,'Password': password})
            print(f"{Fore.BLACK+Back.GREEN}Saving was successful!"+cr)

