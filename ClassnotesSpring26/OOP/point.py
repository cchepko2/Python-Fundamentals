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
    
    # Automatically called when object is "printed"
    def __str__(self) -> str:
        return f"{self.x=}, {self.y=}"

def main():
    a = Point()
    #print(f"{a.x=}, {a.y=}")
    print(a)
    a.x = 101
    print(a)

    print(f'{a.count=}')
    print(f'{Point.count}')

    b = Point(10, 99)
    #print(f"{b.x=}, {b.y=}")
    print(b)

    print(f'{Point.count}')

    b.__del__()
    print(f'{Point.count}')

    print(a)

if __name__ == '__main__':
    main()
        