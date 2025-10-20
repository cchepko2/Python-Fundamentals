'''
Programmer: Corin Chepko
Date: 10/20/25
Program: Create and validate a password
Password requirements: 
    At least 1 digit
    At least 1 uppercase letter
    At least 1 lowercase letter
    At least 1 symbol
    At least 8 characters long
'''

import random
import string

def main():
    MAX_SIZE = 12
    symbols = "!@#$%&*()^"
    all_characters = symbols + string.ascii_letters + string.digits
    password = ""

    while(True):
        password = ""
        for __ in range(MAX_SIZE):
            new_char = random.choice(all_characters)
            password = password + new_char

        # if my password is valid, break the loop
        if(validate_password(password, symbols) == True):
            break
    
    print(f"Here's a password for you: {password}")

def validate_password(password, symbols):
    has_digit = False
    for ch in string.digits:
        if ch in password:
            has_digit = True

    has_lower = False
    for ch in string.ascii_lowercase:
        if ch in password:
            has_lower = True

    has_upper = False
    for ch in string.ascii_uppercase:
        if ch in password:
            has_upper = True

    has_symbol = False
    for ch in symbols:
        if ch in password:
            has_symbol = True

    if(has_symbol and has_digit and has_lower and has_upper):
        #print(f"This password: {password}, is valid!")
        return True
    else:
        #print("Try again")
        return False

if __name__ == '__main__':
    main()





