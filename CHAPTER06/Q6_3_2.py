class Rectangle:
    """長方形"""

    angle = 90

    def __init_(self, width, height):
        self.name = "rectangle"
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        w = self.width
        h = self.height
        return (w + h) * 2

    def calc_area(self):
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.permeter
        a = self.area
        print("name: {}, wight: {}, height: {}, angle: {}".format(n, w, h, ang))
        print("perimeter: {}, area: {}".format(p, a))


class Square(Rectangle):
    """正方形"""

    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"
