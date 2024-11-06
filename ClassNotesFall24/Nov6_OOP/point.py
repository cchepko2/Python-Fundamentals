class Point:
    '''
    Point class, stores x and y coordinates of a point.
    '''
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
    
    def distance(self, another_point):
        dist = ((self.x-another_point.x)**2+(self.y-another_point.y)**2)**0.5
        return f"Distance = {dist}"
    
    def __str__(self):
        # automattically called if printing a class object
        # returns a string
        return f"x = {self.x}, y = {self.y}"


# declare a new Point object, called point1
point1 = Point() 
point2 = Point(3, 0)

print(point1)
print(point1.x, point1.y)

point1.x += 10
point1.y -= 3

print(point1 is point2)
print(point1.x, point1.y)
print(point2.x, point2.y)

point1.x = 0
point1.y = 0

print(point1.distance(point2))

