import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in


# newer and better syntax - preferred way!!
alist = [1, 2, 3]
with open(script_dir+'\\words.txt', 'w') as fout:
    fout.write('apple\nball\ncat\ndog\n')
    fout.write('elephant\n')
    fout.write('zebra\n')
    fout.write(str(1))
    fout.write('\n')
    fout.write(str(alist))