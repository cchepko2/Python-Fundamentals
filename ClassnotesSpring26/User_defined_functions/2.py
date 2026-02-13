def getName():
    name = input("Hi there, enter your full name: ")
    return name

def greet(name):
    print(f'Hello {name}')

name = getName()
greet(name)

# Same operation in one
greet(getName())

