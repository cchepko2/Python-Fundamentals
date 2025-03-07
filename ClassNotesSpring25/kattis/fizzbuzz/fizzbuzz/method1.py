'''
for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 4 == 0:
        string = string + "Buzz"
    if num % 4 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)

for num in range(1,21):
    string = “”
    if num % 3 == 0:
        string = string + “Fizz”
    if num % 5 == 0:
        string = string + “Buzz”
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    print(string)'''

print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,101)),sep='\n')