'''
Corin Chepko
3/26/24
Kattis Problem Roll Call: https://open.kattis.com/problems/rollcall
'''

import sys

#lambda x:(x[0])
def first_name_key(x: list):
    return x[0]

def second_name_key(x: list):
    return x[1]


names = []
fnames = []

for name in sys.stdin:  #this input method leaves the '\n' in the string
   
    if not name or name == '\n':
        break
    
    name = name.strip().split()
    fnames.append(name[0])
    #print(name)
    names.append(name)
    #key = function that returns element to sort by
    names.sort(key=first_name_key)
    names.sort(key=second_name_key)

for name in names:
    if fnames.count(name[0]) > 1:
        print(f"{name[0]} {name[1]}")
    else:
        print(f"{name[0]}")
    
#print(fnames)
#print(names)