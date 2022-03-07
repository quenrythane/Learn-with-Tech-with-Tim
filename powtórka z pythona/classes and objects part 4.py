class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self. x += x
        self. y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return Point(self.x * p.x, self.y * p.y)

    def length(self):
        length = (self.x ** 2 + self.y ** 2) ** (1/2)
        return length

    def __gt__(self, p):  # greater than >
        return self.length() > p.length()


    def __ge__(self, p):  # greater or equal >=
        return self.length() >= p.length()

    def __lt__(self, p):  # less than <
        return self.length() < p.length()

    def __le__(self, p):  # less or equal <=
        return self.length() <= p.length()

    def __eq__(self, p):  # equal ==
        return self.length() == p.length()

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

print(p1.x)
p5 = p1 + p2
print(p5.x)
print(str(p5))
print(p1 > p2)
