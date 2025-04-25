import string

SYMBOLS = "!?$#*@%^"

def validate_password(password):
    DIGITS_REQUIRED = 2
    SYMBOLS_REQUIRED = 1
    CAPS_REQUIRED = 1

    num_digits = 0
    num_symbols = 0
    cap_letters = 0

    for character in password:
        if( character in string.digits):
            num_digits += 1
        if( character in SYMBOLS):
            num_symbols += 1
        if( character in string.ascii_uppercase ):
            cap_letters += 1

    if( num_digits >= DIGITS_REQUIRED and num_symbols >= SYMBOLS_REQUIRED and cap_letters >= CAPS_REQUIRED):
        #print("This is a valid password!")
        return True
    else:
        #print("Not valid")
        return False

def main():
    print("Hello world!")

if __name__ == "__main__":
    main()