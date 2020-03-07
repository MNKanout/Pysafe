"""Python password manger main menu"""
from keys import generate_new_key
from input import accept_user_input
from output import show_saved_logins
from password import generate_password
from reset import delete_all

print('\n\u001b[35mWelcome to PPM!\u001b[0m\nCheck out the \u001b['
      '33mreadme.txt \u001b[0mfile '
      'for info on '
      'how to use this program.\n')

while True:
    user_choice = input('\n\u001b[31mWhat do you wish to do?\u001b['
                        '0m\n1.Generate a new '
                        'encryption key\n2.Enter'
                        ' a new login\n3.Show saved login '
                        'credentials\n4.Generate '
                        'password\n5.Delete all data\n0.Exit\n')
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
        print('Please enter a valid option!')
        continue