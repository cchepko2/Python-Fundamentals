'''
Corin Chepko
3/26/24
Kattis Problem Roll Call: https://open.kattis.com/problems/rollcall
'''

import sys

#lambda x:(x[0])
def first_name_key(x: list):
    return x[0]

names = []
fnames = []

for name in sys.stdin:
   
    if not name or name == '\n':
        break
#while(True):
#    try:
#        name = input()
#    except EOFError:
#        break
#    if not name or name == '\n':  #so I can end the program while testing
#        break
    
    name = name.strip().split()
    #print(name)
    names.append(name)

#names.sort(key=lambda x:(x[0]))
names.sort(key=first_name_key)
names.sort(key=lambda x:(x[1]))

for name in names:
    fnames.append(name[0])
    #lnames.append(name[1])

#print(names)
#print(names)
#print(fnames)
#print(lnames)

for name in names:
    if(fnames.count(name[0]) > 1):
        print(f"{name[0]} {name[1]}")
    else:
        print(name[0])
