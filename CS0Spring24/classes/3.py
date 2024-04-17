class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
    def __str__(self):
        return f"My length is {self.length}, my width is {self.width}\nMy area is {self.area()}\nMy perimeter is {self.perimeter()}."
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return self.length*2+self.width*2

rect1 = Rectangle()
print(rect1)
rect2 = Rectangle(2,3)
print(rect2)
print(rect2.area())

rect4 = Rectangle(4,4)