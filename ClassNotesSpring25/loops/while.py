def game():
    print("You won! Thanks for playing.")

i = 1
while i <= 5:
    print(i, 'Hello World')
    i += 1

play_again = 'y'
while( play_again == 'y'):
    game()

    play_again = input("Do you want to play again? (y/n): ").lower() # convert to lower for easier condition checking

print("Exiting program...Goodbye")

# input validation
integer = input("Enter and integer number: ")
# while the entered number is not a proper digit

while(integer.isdigit() == False):
    integer = input("Invlaid input. Try again: ")

integer = int(integer)
print(f"{integer=}")


# Another way to do input validation, using continue and break statements
while True:
    integer = input('Enter a whole number: ')
    if not integer.isdigit():
        print('Not a valid number!')
        continue
    integer = int(integer)
    break

print(f"{integer=}")

phrase = "the priates of somewhereland."
print(phrase.capitalize())
print(phrase.upper())
print(phrase.title())