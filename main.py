"""
This is a part of the bank module.
Source: https://github.com/Emperor-Shridu/Bank-Module
"""

import menu
import option_commands as oc

"""
This while loop runs till user exits the program.
Here starts the main logic
"""

while True:

    menu.clear_screen()
    menu.h_line()
    
    # This returns the data of the user
    user = menu.first_menu()

    # This returns the option selected from menu and its validity
    option_selected, validity = menu.option_menu()

    menu.h_line()

    # Calling the function according to the option selected
    if validity == 0:
        option_selected = 5

    if option_selected == 1:
        oc.gather_data()

    elif option_selected == 2:
        oc.deposit(user)

    elif option_selected == 3:
        oc.balance_statement(user)

    elif option_selected == 4:
        oc.withdraw(user)

    elif option_selected == 5:
        value = oc.exit_option()
        if value:
            continue
        else:
            quit()


    print("\n\n Done!! Press enter to continue or type anything with enter to exit")
    menu.h_line()

    if input() == "":
        continue
    else:
        break
