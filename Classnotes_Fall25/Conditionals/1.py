def add_two(a, b):
    pass


x = 10
y = 10


if( y > x):
    print("Y is greater than x.")
elif(x > y):
    print("X is grreater than y.")
else:
    print(f"x is equal to y: {(x==y)=}")

if( x == y and x > 0):
    print("x==y and x > 0")

print("Passed the if statement.")


play_again = input("Enter 'y' or 'Y' to play agian: ")
#if( play_again == 'Y' or play_again == 'y'):
if( play_again == 'Y' or 'y'):  # This is always True because 'y' is not zero
    print("Playing again!")