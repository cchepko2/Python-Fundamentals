import pathlib

my_path = pathlib.Path(__file__).parent.resolve()

# This line opens the file, and when the with scope is over, automatically
# closes the file
with open(f'{my_path}/words.txt', 'r') as my_file:
    line = my_file.readline()
    print(line)

# open a text file in WRITE mode
#my_file = open("text.txt", mode='w')
#my_file.close()