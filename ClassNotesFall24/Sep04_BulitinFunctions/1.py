degrees = 0x00b0

print( chr(degrees), 'F', sep='')

print( globals() )

print( hex(ord('°')) )

number = 5

print(id(number))
print(id(5))
print(id(7))

name = "Corin Chepko"
fname, lname = name.split()
print(fname, lname)

line = input("Enter two numbers separated by a space:")
print(line, type(line))
a,b = line.split()
print(a, type(a), b, type(b))
a = float(a)
b = float(b)
print(a+b)



