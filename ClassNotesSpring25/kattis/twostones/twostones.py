import sys

def solution(num):
    if(num%2 == 0):  # if num is even
        even_odd = 'Bob'
    else:
        even_odd = 'Alice'
    return even_odd

print("Enter a number: ", file=sys.stderr)

num = int(input())

even_odd = solution(num)

print(even_odd)