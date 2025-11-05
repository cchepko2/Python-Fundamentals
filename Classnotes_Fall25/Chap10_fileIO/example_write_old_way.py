import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in

print(script_dir)

# old school - not preferred!!
fw = open(script_dir+'\\testing1.txt', 'w') # w is for write mode
fw.write('words\n=====\n')
fw.write('apple\nball\ncat\ndog\n')
print(fw.write('zebra\n'))
fw.close() #must close the file to actually write data
# to the secondoary storage