import sys

def main():
    num1, num2 = collect_two_nums()
    sum = add_two(num1, num2)
    print(sum)

def collect_two_nums():
    '''
    Inputs two numbers, outputs two floats
    '''

    print("Enter two numbers separated by a space: ", file=sys.stderr)
    a, b = input().split()
    a = int(a)
    b = int(b)
    return a, b

def add_two(num_f, num_g):
    return num_f+num_g

# If I'm the main program, run this stuff, otherwise just available for import
if(__name__ == "__main__"):
    main()