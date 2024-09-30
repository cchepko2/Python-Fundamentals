'''
Author: Corin Chepko
Date: 9/30/2024
Program info: Program generates a random password
    password has at least 1 punctuation characters
    password has at least one number
    password has at least 2 uppercase and at least 2 lowercase charater
    password must be 10 characters long
'''

import random
import string
import password_validator as pv  # decided to shorted password_validator to pv

def gen_password():
    
    character_lib = string.ascii_letters+string.digits+string.punctuation
    #print(character_lib)

    password = ""
    #loop to generate 10 random characters
    for i in range(10):
        # add a random character to the password string
        password = password + random.choice(character_lib)
        
    return password

def main():
    #password = input("Enter a password and I'll check it: ")
    while(True):
        password = gen_password()
        #print(password)
        if( pv.password_validator(password) == True):
            break
    print("Your new password is:")
    print(password)
        

if __name__ == "__main__":
    main()