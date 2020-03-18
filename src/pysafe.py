"""Python password manger main menu"""
# Dependencies
from colorama import Fore, Back, init
# Local modules
from keys import generate_key, enter_key
from input import input_login_credentials
from output import output_login_credentials
from password import generate_password
from reset import delete_all
from config import login_credentials_filename, cr, key_filename

init()

if __name__ == '__main__':
    print(f"\n{Fore.BLACK+Back.LIGHTYELLOW_EX+'Pysafe 0.2.0 inbound!'+cr}"
          f"\nCheck out the {Fore.LIGHTRED_EX+'README.md'+cr} "
          f"file for info on how to use this program.")
    while True:
        print('\n'+Fore.BLACK+Back.LIGHTCYAN_EX+'What do you wish to do?'+cr)
        user_choice = input(
                            "1.Generate a new encryption key"
                            "\n2.Use previous encryption key"
                            "\n3.Enter a new login"
                            "\n4.Show saved login credentials"
                            "\n5.Generate password"
                            "\n6.Show locations of saved files"
                            "\n7.Delete all data"
                            "\n0.Exit\n")

        if user_choice == '0':
            exit()
        elif user_choice == '1':
            generate_key()
            continue
        elif user_choice == '2':
            enter_key()
            continue
        elif user_choice == '3':
            input_login_credentials()
            continue
        elif user_choice == '4':
            output_login_credentials()
            continue
        elif user_choice == '5':
            generate_password()
            continue
        elif user_choice == '6':
            print(f'Encryption key file path:'
                  f'{Fore.LIGHTYELLOW_EX}{key_filename}'+cr)
            print(f'Login credentials file path:'
                  f'{Fore.LIGHTYELLOW_EX}{login_credentials_filename}'+cr)
        elif user_choice == '7':
            delete_all()
        else:
            print('\n'+Fore.LIGHTRED_EX+'Please enter a valid option!'+cr)
            continue


