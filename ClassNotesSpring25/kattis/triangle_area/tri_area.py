'''
Corin Chepko
2/3/25
Program: Kattis problem - https://open.kattis.com/problems/triarea
Algorithm Steps:
    Collect two integers, height and base,
        separated by a space
    Convert inputs to intergers
    Calculate area = b*h/2
    print(area)
'''

number_str = input()
height, base = number_str.split()
height = int(height)
base = int(base)
area = base*height/2
print(area)

'''
# Another version, both are fine
height, base = list(map(int, input().split()))
print(height*base/2)
'''