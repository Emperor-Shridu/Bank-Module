""" 
This is a part of the bank module.
This contains the menus to be displayed.
Source: https://github.com/Emperor-Shridu/Bank-Module
"""
import option_commands as oc
import storage_manager

#Constants
MENU_OPTIONS = ["Add account", "Diposit", "Print balance statement", "Withdrawl", "Delete Account", "Exit"]
TOTAL_OPTIONS = len(MENU_OPTIONS)


def h_line():
    """ Prints a horizontal line containing 80 x"""
    print("x"*80)


def clear_screen():
    """ Clears the terminal """
    print("\n"*100)


def ask_to_continue():
    """asks the user to continue"""
    print("\n\n Done!! Press enter to continue or type anything with enter to exit")
    h_line()
    if input() == "":
        clear_screen()
    else:
        oc.exit_option()


def first_menu():
    """
    Asks the user to sign up or login to continue

    :return dict: Dictionary containing data of the user
    """

    while True:
        print("Welcome! You must log in or create a new account to continue.")
        print("1 => Add account \n2 => Login")
        option_chosen = int(input("\n"*3+"please type the option no:"))

        if option_chosen == 1:
            user = oc.gather_data()
            break

        elif option_chosen == 2:
            user_id = int(input("\n\nEnter your id:"))
            password = int(input("Enter the password:"))

            if storage_manager.ispresent(user_id, password):
                user = storage_manager.find(user_id, password)
                break
            else:
                print("\n\ntry again or create a new account")
                h_line()
                continue

        else:
            clear_screen()
            continue
    
    return user


def option_menu():
    """
    print the menu and return the option selected and its validity

    :return int: option selected
    :return bool: 0: forced exit option
                  1: valid option selected
    """

    validity = 1
    print(" Hello and welcome")
    print("How can i help you?", "\n"*4)

    for option_no in range(TOTAL_OPTIONS):
        print(f"{option_no + 1} => {MENU_OPTIONS[option_no]}")

    option_chosen = int(input("\n"*3+"please type the option no:"))

    if option_chosen > 6 or option_chosen <1:
        option_chosen = 6
        validity = 0

    return option_chosen, validity