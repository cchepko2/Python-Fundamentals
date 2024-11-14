"""
Password Validator
Updated By: Seth Kaufman
CSCI 110 Lecture
Date: 25 SEP 2024

Build a password validator that:
- Takes in a string
- Checks for at least 2 uppercase letters
- Checks for at least 2 lowercase letters
- Checks for at least 1 punctuation character
- Checks for at least 1 number
- Checks for length of at least 10

Algorithm:
    1. init counters
    2. 
"""
import string

def passwordValidator ( password:str ) -> str:
    upper_count = 0
    lower_count = 0
    puncutation_count = 0
    number_count = 0

    for char in password:
        if (char in string.ascii_uppercase):
            upper_count += 1
        elif (char in string.ascii_lowercase):
            lower_count += 1
        elif (char in string.punctuation): 
            puncutation_count += 1
        elif (char in string.digits):
            number_count += 1
            
    # Check each condition
    error = ""
    if upper_count < 2:
        error += "Password must contain at least 2 uppercase letters. "
    if lower_count < 2:
        error += "Password must contain at least 2 lowercase letters. "
    if puncutation_count < 1:
        error += "Password must contain at least 1 punctuation. "
    if number_count < 1:
        error += "Password must contain at least 1 number. "
    if len(password) < 10:
        error += "Password must be 10 characters or longer. "
    if len(error) > 0:
        return error

    return "Password is valid."

def main():
    p = input("Provide your password")
    print(passwordValidator(p))
    

main()