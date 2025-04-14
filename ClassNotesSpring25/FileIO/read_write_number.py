
from pathlib import Path

current_file_path = Path(__file__)
#convert current_file_path to a string and add a '\'
# If running Python in a Windows environment, use a '\\', if in a Linux environment (Codespace), 
# use '/' to divide file path from file name.

current_file_path = str(current_file_path.parent) + '\\'


# create a file with 10 integers
# one integer per line
import random

with open(current_file_path + 'integers.txt', 'a') as fout:
    for i in range(10):
        num = random.randint(1, 1000)
        fout.write(str(num) + '\n')

intList = []
with open(current_file_path + 'integers.txt') as fin:
    for i in range(10):
        num = fin.readline().strip()
        if not num:  # if I hit the end of the file, break from reading
            break
        num = int(num)
        intList.append(num)

print(f"{intList=}")

file = current_file_path + 'integers.txt'
with open(file) as f:
    data = f.read()

print(f"{data=}")
        
