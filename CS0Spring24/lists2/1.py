numbers = [3,5,1,20,7,2,2,2]
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(numbers.count(2))

names = ['Jonh', 'Bob', 'Xander']

for i in range(len(names)):
    print(i+1, names[i])

for index, item in enumerate(names):
    print(index+1, item)