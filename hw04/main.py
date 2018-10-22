class Rectangle(object):
    def __init__(self,a,b):
        self.width=a
        self.height=b

    def area(self):
        return self.width*self.height

class Ellipse(object):
    def __init__(self,a,b):
        self.width=a
        self.height=b

    def area(self):
        return self.width*self.height*3.14

class Square(Rectangle):
    def __init__(self,a):
        self.width=a
        self.height=a

class Circle(Ellipse):
    def __init__(self,a):
        self.width=a
        self.height=a

def compute_area(shapes):
    return sum([x.area() for x in shapes])

shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]

total_area=compute_area(shapes)

print(total_area)
