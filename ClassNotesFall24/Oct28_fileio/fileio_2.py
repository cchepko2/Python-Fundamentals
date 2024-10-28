import pathlib
import random

my_path = pathlib.Path(__file__).parent.resolve()
readfile_name = f'{my_path}/words.txt'

# This line opens the file, and when the with scope is over, automatically
# closes the file
with open(readfile_name, 'r') as my_file:
    line = "not empty"
    lines = []
    while( line != ""):
        line = my_file.readline().strip()
        if(line == ""):
            break
        lines.append(line)
        

print(lines)
print("Finished with file!")

print("Here's a random word from the words file: ")
print(random.choice(lines))