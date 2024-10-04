names = input("Please enter your full name: ").split()

print(names)

fname, lname = names  # unpacking items in names into varibles 
                      #  fname and lname
name1 = names[0]  # accessing individual items in tuple
name2 = names[1]
print(name1, name2)
# when unpacking, there must be the same number of varibles as 
# items in the tuple or list

print(fname, lname, "Items in names =",len(names))
print("Corin" in names)
# swap values of two variables
a = 100
b = 200
temp = a
a=b
b=temp

print(a,b)
a, b = b, a  # swapping varibles is easier with tuples
print(a,b)
