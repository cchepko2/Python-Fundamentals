import os
script_dir = os.path.dirname(__file__)

print(__file__)

filename = script_dir + '\\program.txt'
with open(filename, 'r') as fin:
    program = fin.readlines()

filename = script_dir + '\\out_program.txt'
with open(filename, 'w') as fout:
    line_num = 1
    for line in program:
        new_line = f"{line_num:04d} {line}"
        fout.write(new_line)
        line_num += 1