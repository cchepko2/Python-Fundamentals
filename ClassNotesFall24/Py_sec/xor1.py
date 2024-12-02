in_string = 'label'


new_str = ''
for c in in_string:
    new_str += chr(ord(c) ^ 13)

print(new_str)

