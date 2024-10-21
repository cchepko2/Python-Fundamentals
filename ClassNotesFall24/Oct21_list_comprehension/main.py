# constructing a list of X**2 from x = 1 to 10

empty_list = []
for i in range(1,11):
    empty_list.append(i**2)

for num in empty_list:
    print(num)

# This does the same thing as above lines 3-5
python_xpert_list = [x**2 for x in range(1,11)]

for num in python_xpert_list:
    print(num)