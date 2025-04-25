class Point:
    """
    Point class to represent and manipulate x and y in 2D coordinates
    """
    count = 0 # class variable/attribute
    
    # constructor to customize the initial state of an object
    # first argument refers to the instance being manipulated;
    # it is customary to name this parameter self; but can be anything
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        # x and y are object variables/attributes
        self.x = xx
        self.y = yy
        Point.count += 1 # increment class variable
    # destructor 
    def __del__(self):
        Point.count -= 1

    def __str__(self):
        return f"{self.x=} and {self.y=}"
    
    def dist_from_origin(self):
        import math
        dist = math.sqrt(self.x**2+self.y**2)
        return dist

    def dist_from_point(self, b):
        import math
        dist = math.sqrt((self.x-b.x)**2+(self.y-b.y)**2)
        return dist

a = Point()
print(f"{a.x=}, {a.y=}")
print(f"{Point.count=}")

b = Point(2, 5)
print(f"{b.x=}, {b.y=}")
print(f"{Point.count=}")

b.__del__()
print(f"{Point.count=}")
print(f"{b.x=}, {b.y=}")


a.x = 3
a.y = 4
b.x = 0
b.y = 0

print(a)
print(f"{a.dist_from_origin()=}")
print(f"{a.dist_from_point(b)=}")