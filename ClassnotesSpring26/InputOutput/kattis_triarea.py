'''
Corin Chepko
1/28/26
Kattis Problem - Triarea: https://open.kattis.com/problems/triarea
Algorithm Steps:
    input two numbers separated by a space
    convert each number into an integer
    calculate the area = height*base/2
    print(area)
'''

#Will have remove input message before kattis submission
numbers = input()
#print(numbers)
#print(numbers.split())
height, base = numbers.split()
#print(height, base)

height = int(height)
base = int(base)
area = 1/2*height*base
print(area)