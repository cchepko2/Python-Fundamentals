def addtwo(a, b):
    a = 3
    print(a, b)
    return a+b

def addtwo_list(a, b):
    a = b
    a.append("Hello")
    print(a, b)
    return a+b

a=5
b=2

list_a = [1, 2]
list_b = [3, 4]
addtwo_list(list_a, list_b)
print(list_a, list_b)