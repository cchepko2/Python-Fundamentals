play_again = 'y'

if( play_again == 'y'):
    print(f"{play_again=}")

if( play_again == 'y' and play_again == 'Y'):
    print(f"{play_again=}")
else:
    print("play_again cannot be 'Y' and 'y' ")

# Always true because the second condition is does not specify 'play_again =='
# interprets just 'Y' to be non-zero, thus True
if( play_again == 'y' or 'Y' ): 
    print(f"{play_again=}")
    print("This conditional is always true")

cancel = False
if( play_again == 'y' and cancel == False):
    print("play_again == 'y' and user didn't cancel program.")

number = int(input("Enter a whole number: "))

if( number%2 == 0): # if number even
    if(number > 0 ): # is number above zero
        print("number is even and positive")
    elif( number < 0 ):
        print("number is even and negative")
    else:
        print("number is 0")
else: # number is not even
    if(number > 0 ): # is number above zero
        print("number is odd and positive")
    else:
        print("number is odd and negative")
    