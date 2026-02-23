'''
Corin Chepko
2/23/26
Program: Add Two Numbers:
    input two numbers
    convert to float
    print sum of the numbers
'''

def main():
    numbers = input("Enter two numbers separated by a space: ").split()
    print(f"{numbers=}")
    number1, number2 = map(float, numbers)

    answer = add_two(number1, number2)
    print(number1, "plus", number2, "=", answer)

def add_two(num1, num2):
    return num1+num2

def test():
    assert(add_two(2, 3) == 5)
    assert(add_two(0, 0) == 0)
    assert(add_two(99, 1) == 100)
    print("All tests passed!")

if __name__ == "__main__":
    test()
    main()