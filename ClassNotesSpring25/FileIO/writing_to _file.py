'''
Write some text to file
'''

from pathlib import Path

current_file_path = Path(__file__)
#convert current_file_path to a string and add a '\'
current_file_path = str(current_file_path.parent)+'\\'

# newer and better syntax - preferred way!!
alist = [1, 2, 3]
with open(current_file_path+'words.txt', 'w') as fout:
    fout.write('apple\nball\ncat\ndog\n')
    fout.write('elephant\n')
    fout.write('zebra\n')
    fout.write(str(1))
    fout.write('\n')
    fout.write(str(alist))