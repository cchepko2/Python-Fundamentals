'''
Uses a defined function get_name() to collect a name a return the data to the 
main program
'''


def getname(name):
    name = input("Enter your name please: ")
    return name

#def rectangle_area(side_a, side_b):
def rectangle_area(side_a: float, side_b: float) -> float:
    return side_a*side_b
    

name = "Corin"
getname(name)
print(f"Hello again {name}!")

a, b = input("Enter two sides of a rectangle: ").split()
a = float(a)
b = float(b)

#a, b = map(float, input("Enter two sides of a rectangle: ").split())
print("The area is", rectangle_area(a, b))

#print(locals())
#print(globals())
