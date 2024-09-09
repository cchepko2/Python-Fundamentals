# print is a fruitless function: it does nto return anything, if asked it returns <None>

# fruitless function, take no parameters and returns nothing
def long_greeting():
    print("Hello and blah blah blah...")

def add_two(num1: int,  num2: int) -> int:
    sum = num1+num2
    num1 = 15
    return sum

long_greeting()
long_greeting()
long_greeting()

a,b = input("Enter two numbers separated by a space.").split()

#a = int(a)  can convert one at a time, or use map function to convert all
#b = int(b)
a,b = map(int, (a,b))

print(a, b)
print( add_two(a, b) )
print(a, b)
