'''
FileIO opening and closing and paths
'''

import os

# This is the file being run
print(f"{__file__=}")

# Strip the filename and return the path
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
print(f'{script_dir=}')

# For windows based system
filename = script_dir + "\\data.txt"

# For linux based system (codespaces)
filename = script_dir + "//data.txt"

with open(filename, 'w') as fout:
    fout.write("Hello ")
    fout.write("World!\n")
    fout.write("This is line 2")

print()
print()

# Read whole file into string
with open(filename) as fin:
    contents = fin.read()
    print(f'{contents=}')

# Read file into list of string lines
with open(filename) as fin:
    lines = fin.readlines()
    print(f'{lines=}')

# Read file one line at a time
with open(filename) as fin:
    line = fin.readline()
    print(f'First line = {line=}')

# Read file one line at a time
with open(filename) as fin:
    for line in fin:
        # Take off newline character
        #line = line.strip()
        print(f'{line=}')

