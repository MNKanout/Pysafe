"""Python password manger main menu"""
from keys import generate_new_key
from input import accept_user_input
from output import show_saved_logins
from password import generate_password
from reset import delete_all
from colorama import Fore, Back


print(f"\n"
      f"{Fore.BLACK+Back.LIGHTCYAN_EX+'Pysafe inbound!'+ Fore.RESET+Back.RESET}"
      f"\nCheck out the {Fore.LIGHTYELLOW_EX +'README.md'+ Fore.RESET} "
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
        exit()
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