"""Python password manger main menu"""
# Dependencies
from colorama import Fore, Back
# Local modules
from keys import generate_key
from input import input_login_credentials
from output import output_login_credentials
from password import generate_password
from reset import delete_all
from config import cr

def main():
    """Main menu for pysafe"""
    print(f"\n"
          f"{Fore.BLACK+Back.LIGHTCYAN_EX+'Pysafe inbound!'+Fore.RESET+Back.RESET}"
          f"\nCheck out the {Fore.LIGHTYELLOW_EX+'README.md'+cr} "
          f"file for info on how to use this program.")

    while True:
        print('\n'+Fore.BLACK+Back.MAGENTA+'What do you wish to do?'+cr)
        user_choice = input(
                            "1.Generate a new encryption key"
                            "\n2.Enter a new login"
                            "\n3.Show saved login credentials"
                            "\n4.Generate password"
                            "\n5.Show locations of saved files"
                            "\n6.Delete all data"
                            "\n0.Exit\n")

        if user_choice == '0':
            exit()
        elif user_choice == '1':
            generate_key()
            continue
        elif user_choice == '2':
            input_login_credentials()
            continue
        elif user_choice == '3':
            output_login_credentials()
            continue
        elif user_choice == '4':
            generate_password()
            continue
        elif user_choice == '5':
            print(f'Encryption key file path:'
                  f'{Fore.LIGHTYELLOW_EXkey_filename}'+cr)
            print(f'Login credentials file path:'
                  f'{Fore.LIGHTYELLOW_EXlogin_credentials_filename}'+cr)
        elif user_choice == '6':
            delete_all()
        else:
            print('\n'+Fore.LIGHTRED_EX+'Please enter a valid option!'+cr)
            continue


main()