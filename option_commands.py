""" 
This is a part of the bank module.
This contains the functionalities for the option selected.
Source: https://github.com/Emperor-Shridu/Bank-Module
"""
from random import randrange
import storage_manager

#constants
FIELDS = ["Acc no", "Acc Type", "Name", "Balance"]
TOTAL_FIELDS = len(FIELDS)


def gather_data():
    """
    gather the required data to create the account (one at a time) and store it in database

    :return dict:  dict that would contain the data of new account
    """

    print("\n"*2+"You have to fill the following form to add your account :")


    name = input("Enter the name of the owner of account:")
    acc_type = input("Enter the type of account you want to create(savings\\business): ")
    balance = int(input("Enter the balance you want to start with:"))
    account_no = randrange(9999999, 1000000000)
    password = randrange(99999, 1000000)
    # validating uniqueness
    try:
        while storage_manager.ispresent_by_accNo(account_no):
            randrange(9999999, 1000000000)
    except FileNotFoundError:
        pass
    #file not existing means no record is created so uniqueness already verified


    account_details = {"Acc no":account_no, "Acc Type":acc_type, "Name":name, "Balance":balance, "password":password}
    storage_manager.store(account_details)


    print("\n"*2+"Congratulations your account has been created\n\
        remember your password:", password, "\n \tAnd Acc Number:", account_no)

    return account_details


def exit_option():
    """
    asks if user wanna continue, else exits
    :return bool: 0: Not wanting to continue
                  1: Wants to continue
    """

    a = input("Do you not wanna continue :(   (y/n)")
    if a == "y":
        return 1
    else:
        return 0
    print("You have successfully exited\n\n")
    a = input("Do you want logs?(y/n)")
    if a == "y":
        log.logs()
    print("Thanks for using, have a great day!!")


def deposit(user):
    """
    Deposits and records in database, the money submitted by user.

    :param dict user: The dictionary containing the data of the user
    """

    amount_submitted = int(input("Enter the ammount you want to deposit:"))
    user["Balance"] += amount_submitted
    print("Bravo, you got the amount in the safe hands.")
        

def balance_statement(user):
    """
    Prints the balance statement of the user.

    :param dict user: The dictionary containing the data of the user
    """

    for x in range(TOTAL_FIELDS):
        print(f"Your {FIELDS[x]} = {user[FIELDS[x]]}")

def withdraw(user):
    """
    Withdraws and records in database, the money submitted by user. Prints error if balance
    is less than money to be withdrawn

    :param dict user: The dictionary containing the data of the user
    """

    amount = int(input("Enter the ammount you want to withdraw:"))

    if amount <= int(user["Balance"]):
        user["Balance"] -= amount
        print("Bravo, you got the amount in your hands.")

    else:
        print("Not enough money to continue")