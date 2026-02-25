'''
Variable and function scope
'''

import math

# PI will be a global variable accessed by all functions in this file
PI = math.pi

# global scope = all non-indented variables and functions
def main():
    # use global PI variable instead of the local PI
    PI = 2*3.14159
    print(PI)
    greet()
    name = "Susan"
    print(PI)

    sum = PI + PI
    print(sum)

    numbers = [1, 2]
    print(sum(numbers))

def greet():
    import random
    name = "Jack"
    print(name)
    print(PI)
    print(random.randint(1, 10))

if __name__ == "__main__":
    main()