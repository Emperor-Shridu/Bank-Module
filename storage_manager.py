""" 
This is a part of the bank module.
This manages the data.
Source: https://github.com/Emperor-Shridu/Bank-Module
""" 
# i used comma instead of colon and wasted half an hour :( line 22

def store(user):
    """ 
    This stores the user's data in database
    
    :param dict user: dictionary containing user data
    """

    with open("storage.txt", "a") as f:
        f.write(str(user) + "\n")

def ispresent(accNo, password):
    """ 
    This checks the presence of user data in database.
    
    :param int accNo: account number of that account
    :param int password: password of that account

    :return bool: 0: Not present
                  1: Present
    """
    with open("storage.txt", "r") as f:
        text = f.read()
        start_index = text.find("{'Acc no': "+ str(accNo))

        if start_index == -1:
            print("invalid id")
            return 0
        else:
            end_index = text.find("}", start_index)
            user = eval(text[start_index: end_index+1])
            if user["password"] == password:
                return 1
            else:
                print("invalid password")
                return 0

def find(accNo, password):
    """ 
    This gives the data of user if present in database.
    
    :param int accNo: account number of that account
    :param int password: password of that account

    :return dict: dictionary containing the user data (if present)
    """

    if ispresent(accNo, password):

        with open("storage.txt", "r") as f:

            text = f.read()
            start_index = text.find("{'Acc no': "+ str(accNo))
            end_index = text.find("}", start_index)
            user = eval(text[start_index: end_index+1])
            return user

    else:
        print("user not registered")


def ispresent_by_accNo(accNo):
    """ 
    This checks if id is present in database.
    
    :param int accNo: account number of that account

    :return bool: 0: id not present
                  1: id present
    """

    with open("storage.txt", "r") as f:
        text = f.read()
        start_index = text.find("{'Acc no': "+ str(accNo))

        if start_index == -1:
            print("invalid id")
            return 0
        else:
            return 1


def delete_record(accNo, password):
    """ 
    This deletes the user data from database.
    
    :param int accNo: account number of that account
    :param int password: password of that account

    """

    #source 1 : https://www.geeksforgeeks.org/how-to-delete-data-from-file-in-python/
    #source 2 : https://stackoverflow.com/questions/7356043/how-to-delete-specific-strings-from-a-file

    # better methods are welcomed, until then:
    with open("storage.txt", "r") as f:

        all_lines = f.readlines()
        # + "\n" took half an hour
        delete_line = str(find(accNo, password)) + "\n"

    with open("storage.txt", "w") as f:

        f.truncate()
        
        for line in all_lines:
            if line == delete_line:
                continue
            else:
                f.write(line)
