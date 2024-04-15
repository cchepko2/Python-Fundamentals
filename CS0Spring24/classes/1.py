import math

class Point:
    count = 0 # class variable/attribute

    def __init__(self, xx=0, yy=0):
        self.x = xx
        self.y = yy
        Point.count +=1
    
    def __del__(self):
        Point.count -=1
    
    def __str__(self):
        return f"x={self.x}, y={self.y}"
    
    def dist_from(self,point_b):
        return math.sqrt((self.x-point_b.x)**2 + (self.y-point_b.y)**2)

def main():
    a = Point()
    b = Point(1,1)
    c = Point(2,3)

    print(a.x, a.y)
    print(b.x, b.y)
    print(Point.count)

    b.__del__()
    print(b.x, b.y)
    print(Point.count)

    print(a)

    print(f"Point b is {a.dist_from(b)} from point b.")


if __name__ == '__main__':
    main()