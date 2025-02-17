import sys

name = "Corin" # A variable that is not indented is a global variable
        # Global variables can be accessed by any function

def main():
    num1, num2 = collect_two_nums()
    print(name)
    sum = add_two(num1, num2)
    print(sum)

def collect_two_nums():
    '''
    Inputs two numbers, outputs two floats
    '''
    # use global to force function to use global variable
    name = "John"
    print(f"Hello {name}, enter two numbers separated by a space: ", file=sys.stderr)
    a, b = input().split()
    a = int(a)
    b = int(b)
    return a, b

def add_two(num_f, num_g):
    sum = num_f+num_g
    num_f = 10
    num_g = 6
    return sum

# If I'm the main program, run this stuff, otherwise just available for import
if(__name__ == "__main__"):
    main()