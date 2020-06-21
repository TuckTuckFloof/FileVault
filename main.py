'''
    Input a username and password to access the file of choice
    If the username and password is incorrect, then it denies access
    If the information is correct, then the Vault opens
    When vault is openend, it should be able to add, delete, and edit files but for editing we could just use g-edit or something idk
'''
from os import path

def main():
    # Idk if I want to put these here, but it's basically to declare them now so I don't have to later
    username = ''
    password = ''
    
    try:
        returner = input("Have you used this File Vault before? (Y/N)\n")

        # The person is returning to the program
        if returner.upper() == 'Y':
            print('Awesome, what file would you like to access?')
            infile_name = input()
            # Makes sure that the txt extension is added 
            if '.txt' not in infile_name:
                infile_name = infile_name + '.txt'
            path.isfile(infile_name)

        elif returner.upper() == 'N':
            print('Well then welcome! Please enter a username')
    except ValueError:
        print('Please enter a valid input')
        main()