''' WRONG
def add_two():
    n1, n2 = input("Enter two numbers spearated by a space: ").split()
    n1 = float(n1)
    n2 = float(n2)
    print(n1+n2)
'''

''' RIGHT '''
def add_two(n1, n2):
    sum = n1 + n2
    return sum


n1, n2 = input("Enter two numbers spearated by a space: ").split()
n1 = float(n1)
n2 = float(n2)

sum = add_two(n1, n2)
print(f"Sum of {n1} and {n2} = {sum}")


#diff = diff_two(n1, n2)

