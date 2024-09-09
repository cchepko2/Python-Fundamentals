import string

print( string.ascii_letters )
print(string.digits)
print(string.punctuation)

user_input = input("Enter in the object (hint: answer is house). Make sure to use all lower case!\n")

print(string.ascii_uppercase)

if( string.ascii_uppercase in user_input):
    print("You did not use all lower case!")

if( user_input == 'house' or user_input == 'House' or user_input == "HOUSE"):
    print("You've guess the answer!!!!!")
else:
    print("Can you read a hint?")

if( user_input.lower() == 'house'):
    print("You've guess the answer!!!!!")
else:
    print("Can you read a hint?")

