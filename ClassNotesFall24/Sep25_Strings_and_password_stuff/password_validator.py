"""
Password Validator
Updated By: Corin Chepko
CSCI 110 Lecture
Date: 30 SEP 2024

Build a password validator that:
- Takes in a string
- Checks for at least 2 uppercase letters
- Checks for at least 2 lowercase letters
- Checks for at least 1 punctuation character
- Checks for at least 1 number
- Checks for length of at least 10

Algorithm:
    1.
"""

import string

# function return True if valid, False if invalid
def password_validator(password : str) -> bool:
    num_upper = 0
    num_lower = 0
    num_punc = 0
    num_nums = 0

    for c in password:
            if c in string.punctuation:
                num_punc += 1
            if c in string.ascii_lowercase:
                num_lower += 1
            if c in string.ascii_uppercase:
                num_upper += 1
            if c in string.digits:
                num_nums += 1

    if(len(password) >= 10 and num_upper >= 2 and num_lower >=2 and num_punc >= 1 and num_nums >= 1):
        print("Valid password!")
        return True
    else:
        print("Invalid password...")
        if( len(password) < 10):
            print("Password less than 10 characters.")
        if(num_upper < 2):
            print(f"Only {num_upper} upper case characters.")
        if(num_lower < 2):
            print(f"Only {num_lower} lower case characters.")
        if(num_punc < 2):
            print(f"Only {num_punc} punctuation characters.")
        if(num_nums < 1):
            print(f"Only {num_nums} digits.")
        return False

def main():
    password = input("Enter a password and I'll check it: ")
    password_validator(password)

if __name__ == "__main__":
    main()