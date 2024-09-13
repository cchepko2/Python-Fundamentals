def addTwo(num1, num2):
    sum = num1+num2
    num1 = 15
    return sum

a,b = map(int,input("Enter two numbers separated by a space").split())

print("a = {} and b = {}".format(a, b))

sum = addTwo(a,b)

print("a = {} and b = {}".format(a, b))
