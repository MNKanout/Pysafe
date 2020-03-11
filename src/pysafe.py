"""Python password manger main menu"""
from src.keys import generate_new_key
from src.input import accept_user_input
from src.output import show_saved_logins
from src.password import generate_password
from src.reset import delete_all
from colorama import Fore, Back


print(f"\n"
      f"{Fore.BLACK+Back.LIGHTCYAN_EX+'Pysafe inbound!'+ Fore.RESET+Back.RESET}"
      f"\nCheck out the {Fore.LIGHTYELLOW_EX +'readme.txt'+ Fore.RESET} "
      f"file for info on how to use this program.")

while True:
    print(Fore.LIGHTRED_EX + '\nWhat do you wish to do?')
    user_choice = input(
                        "1.Generate a new encryption key"
                        "\n2.Enter a new login"
                        "\n3.Show saved login credentials"
                        "\n4.Generate password"
                        "\n5.Delete all data"
                        "\n0.Exit\n")

    if user_choice == '0':
        break
    elif user_choice == '1':
        generate_new_key()
        continue
    elif user_choice == '2':
        accept_user_input()
        continue
    elif user_choice == '3':
        show_saved_logins()
        continue
    elif user_choice == '4':
        generate_password()
        continue
    elif user_choice == '5':
        delete_all()
    else:
        print(Fore.LIGHTRED_EX +'Please enter a valid option!')
        continue