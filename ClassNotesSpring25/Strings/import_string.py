import string #gives various strings and string functions

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)
print(string.hexdigits)
print(f"{string.whitespace=}")
print(string.capwords("capitalize on it!"))

while(True):
    digits = input("Enter some digits (whole number): ")
    if digits.isdigit():
        break
    else:
        print("Please try again...enter digits: ")

print(digits)

while(True):
    float_digits = input("Enter some digits: ")
    try:
        float_digits = float(float_digits)
    except:
        print("Error: you are too exceptional!")
        float_digits = 0
    break
    
    '''if float_digits.isnumeric():
        break
    else:
        print("Please try again...enter digits: ")'''

print(float_digits)

print(list(string.ascii_letters))

