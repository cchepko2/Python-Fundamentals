# Global and local scope demo
name = "Alice" # global variable
name1 = "Xander" # global variable

def someFunc(a, b):
    global name
    name = "Jhon"  # local (unless 'global' keyword is used previously) 
                   # name belonging to 'someFunc' function
    print(f'{name = }') # Access global variable, name
    name1 = "John" # Declare local variable
    print(f'{a=} and {b=}') # a and b are local variables
    print(f'Hello {name1}') # Access local variable, name1

someFunc(1, 'Apple')

print()
print(name) # Access global variable name
print(name1) # Can you access name1 which is local to someFunc function?