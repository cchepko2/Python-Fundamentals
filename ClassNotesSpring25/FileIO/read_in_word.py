from pathlib import Path
import random

current_file_path = Path(__file__)
#convert current_file_path to a string and add a '\'
# If running Python in a Windows environment, use a '\\', if in a Linux environment (Codespace), 
# use '/' to divide file path from file name.

current_file_path = str(current_file_path.parent) + '\\'

# by default files open in read and text mode 
words = []
with open(current_file_path+'words2.txt') as fin:
    data = fin.readlines()
    for word in data:
        words.append(word.strip())

print(f"{words=}")
print(f"Random word is: {random.choice(words)}")