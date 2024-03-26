'''
Corin Chepko
3/26/24
Kattis Problem Roll Call: https://open.kattis.com/problems/rollcall
'''

import sys

names = []
for name in sys.stdin:
   
    if not name or name == '\n':
        break
    
    name = name.strip().split()
    #print(name)
    names.append(name)

names.sort(key=lambda x:(x[0]))
names.sort(key=lambda x:(x[1]))
#print(names)

for name in names:
    if(name[0] in names[0]):
        print(f"{name[0]} {name[1]}")
    else:
        print(name[0])
