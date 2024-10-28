import pathlib

my_path = pathlib.Path(__file__).parent.resolve()

# This line opens the file, and when the with scope is over, automatically
# closes the file
with open(f'{my_path}/words.txt', 'r') as my_file:
    lines = my_file.readlines()
    
stripped_words = []
for line in lines:
    stripped_words.append(line.strip())
print(stripped_words)
print("Finished with file!")

with open(f'{my_path}/words.txt', 'r') as my_file:
    lines = my_file.read()
    lines_list = lines.split('\n')

print(lines_list)


# With the 'with' statement done, the file is automatically close