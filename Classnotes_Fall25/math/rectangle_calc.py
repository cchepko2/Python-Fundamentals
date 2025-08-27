'''
Program: Calculates the perimeter and area of
        a rectangle.
Algorithm Steps: 
    Input length and width
    convert to float values
    calculate periemter and area
    print values
'''

length = input("Please enter the length of the rectangle: ")
length = float(length)  # Convert from str to float

width = input("Please enter the width of the rectangle: ")
width = float(width)  # Convert from str to float

perimeter = 2*length + 2*width
area = length * width

solution = "The area is " + str(area) + " and the periemter is " + str(perimeter)
print(solution)
print("The area is ", area," and the periemter is ", perimeter)