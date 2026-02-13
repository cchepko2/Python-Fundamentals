def add_two(num1, num2):
    sum = num1 + num2
    return sum

fname = "Corin"
lname = "Chepko"

print(add_two(fname, lname))

n1, n2 = map(float, input("Enter two numbers separated by a space: ").split())

n1 = float(n1)
n2 = float(n2)

print("The sum of", n1, "and", n2, '=', add_two(n1, n2))
