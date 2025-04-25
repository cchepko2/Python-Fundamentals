import verify_pw as verify_pw
import random
import string

symbols = verify_pw.SYMBOLS

def main():
    num_characters = 12
    combined_chars = list(symbols+string.ascii_uppercase+string.ascii_lowercase+string.digits)

    new_password = ""
    while( verify_pw.validate_password(new_password) == False ):

        new_password = ""
        for i in range(num_characters):
            new_password += random.choice(combined_chars)
            #new_password.append(random.choice(combined_chars))

        #print(new_password)
        #print(verify_pw.validate_password(new_password))
    print(f"{new_password=}")

if __name__ == "__main__":
    main()