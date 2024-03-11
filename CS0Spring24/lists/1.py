#list = ['hello', 2.0, 10, [10, ('hi', 'world'), 3.5], (1, 'uno')]
#never use list as a variable or function name

list2 = [2,5,6,8,0]

names = ["Corin", "Alice", "Xander", "Bob"]

for i in range(1, len(names)):
    print(names)
    if names[i] < names[i-1]:
        temp = names[i]
        names[i] = names[i-1]
        names[i-1] = temp
print(names)

name = "Corin"
#name[-1] = 'm' cannot modify elements in a string

print(list2)

list1 = list(range(10))
print(max(list1))
print(max(list2))

#max = 99  this would overwite the max() python function
print(max(list2))