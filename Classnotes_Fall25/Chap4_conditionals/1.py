x = 10
y = 11

if( x != y):  # one way selector
    print("x is not equal to y")

x = y
if( x != y): # Two way selector 
    print("x is not equal to y")
else:
    print("x == y")

day = 0
if( day == 0 ):
    print("It's Monday")
elif( day == 1 ):
    print("It's Tuesday")
elif( day == 2 ):
    print("It's Wednesday")
elif( day == 3 ):
    print("It's Thursday")
elif( day == 4 ):
    print("It's Friday")
elif( day == 5 ):
    print("It's Saturday")
else:
    print("It's Sunday")

again = 'n'
# if(again == 'y' or 'Y') This statement is always True 
                        # because 'Y' is not a condition and is not False 
if( again == 'y' or again == 'Y'): # Always use full conditions
    condition = (x == y)
    print(f"{x} == {y} = {condition}")