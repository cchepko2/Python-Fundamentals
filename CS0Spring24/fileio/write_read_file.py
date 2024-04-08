import pathlib

my_path = pathlib.Path(__file__).parent.resolve()
filename = 'out_file.txt'
full_fileName = f"{my_path}/{filename}"
print(full_fileName)
full_filename = 'C:\\Users\\cchep\\CS110\\Python-Fundamentals\\CS0Spring24\\fileio\outfile.txt'
print(full_fileName)

file_obj = open(filename, 'a')

lname = "More"
file_obj.write("Add\n")
file_obj.write(lname)
file_obj.close()

file_obj = open(f"{my_path}/words.txt", 'r')
line=file_obj.readline()
print(line)

lines = file_obj.readlines()
print(lines)

file_obj.close()