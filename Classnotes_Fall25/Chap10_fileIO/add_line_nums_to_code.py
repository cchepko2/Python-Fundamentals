import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

with open(script_dir+'\\out_program.txt', 'w') as fout: 
    with open(script_dir+'\\program.txt', 'r') as fin:
        line_num = 1
        for line in fin:
            new_line = f"{line_num:04d} {line}"
            #new_line = f"{str(line_num):<5} {line}"
            fout.write(new_line)
            line_num += 1
