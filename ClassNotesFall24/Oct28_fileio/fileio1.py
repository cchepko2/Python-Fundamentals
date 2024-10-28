import pathlib

my_path = pathlib.Path(__file__).parent.resolve()

# This line opens the file, and when the with scope is over, automatically
# closes the file
with open(f'{my_path}/words.txt', 'r') as my_file:
    line = my_file.readline()
    line = line.strip()
    print(line)

    print(line == "apple")
'''    while( line != ''):
        line = my_file.readline()
        print(line)'''

print("Finished with file!")

# With the 'with' statement done, the file is automatically close