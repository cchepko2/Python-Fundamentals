def add_two(a,b):
    return a+b

again = 'y'


while(again.lower() == 'y'):
    a,b = map(float, input("Enter two numbers separated by a space: ").split())
    print(f"Hello again! {a} + {b} = {add_two(a,a)}")
    
    again = input("Loop again? Enter 'Y' or 'y' to repeat.")


i = 0
while(i<10):
    print(i)
    i+=2


