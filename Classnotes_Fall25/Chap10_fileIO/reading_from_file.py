import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


# newer and better syntax - preferred way!!
with open(script_dir+'\\words.txt', 'r') as fin:
    text = fin.read()  # This is a string
    lines = text.split() # this is a list of lines

    fin.seek(0)
    lines2 = fin.readlines()

print(lines)
print(lines2)
