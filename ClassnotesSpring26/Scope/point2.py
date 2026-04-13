'''
A more complete Point class with getters and setters
'''

class Point:
    """
    Point class represents and manipulates x,y coords
    """
    count = 0
    
    def __init__(self, xx=0, yy=0):
        """Create a new point with given x and y coords"""
        self.x = xx
        self.y = yy
        Point.count += 1

    def get_point(self):
        return (self.x, self.y)

    def set_point(self,xx,yy):
        self.x = xx
        self.y = yy
    
    def dist_from_origin(self):
        import math
        dist = math.sqrt(self.x**2+self.y**2)
        return dist
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    # destructor 
    def __del__(self):
        Point.count -= 1

def change_point(a: Point):
    a.set_point(99999, 99999)

def main():    
    a = Point(1,1)
    b = Point()
    b.set_point(99, 99)
    print(a)
    print(b)

    change_point(a)
    print(a)


if __name__ == '__main__':
    main()