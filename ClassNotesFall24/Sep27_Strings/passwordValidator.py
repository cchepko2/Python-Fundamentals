"""
Password Validator
Updated By: Seth Kaufman
CSCI 110 Lecture
Date: 27 SEP 2024

Build a password validator that:
- Takes in a string
- Checks for at least 2 uppercase letters
- Checks for at least 2 lowercase letters
- Checks for at least 1 punctuation character
- Checks for at least 1 number
- Checks for length of at least 10

Algorithm:
    1. init counters
    2. create loop to look at each character in string  
    3. check if each character is an upper, lower, punucation or number
    4. check if there an error and print out message is the password does not match
    5. print out error/success message
"""
import string

def passwordValidator(password:str):
    #create counter trackers for each test case
    upper_count = 0
    lower_count = 0
    puncutation_count = 0
    number_count = 0
    
    # create loop to look at each character in string  
    for c in password:
        #check if each character is an upper, lower, punucation or number
        if (c in string.ascii_uppercase):
            upper_count += 1
        elif (c in string.ascii_lowercase):
            lower_count += 1
        elif (c in string.punctuation): 
            puncutation_count += 1
        elif (c in string.digits):
            number_count += 1 
    
    # check if there an error and print out message is the password does not match
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

    # print out success message
    return "Password is valid."
    
    
def main():
    p = input("Provide your password: ")
    print(passwordValidator(p))
    

main()