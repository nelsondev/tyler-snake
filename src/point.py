class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, a):
        return Point(self.x + a.x, self.y + a.y)
    def __sub__(self, a):
        return Point(self.x - a.x, self.y - a.y)
    def __mul__(self, a):
        return Point(self.x * a.x, self.y * a.y)
    def __truediv__(self, a):
        return Point(self.x / a.x, self.y / a.y)
    
    def __lt__(self, a):
        return self.x < a.x and self.y < a.y
    def __gt__(self, a):
        return self.x > a.x and self.y > a.y
    def __eq__(self, a):
        return self.x == a.x and self.y == a.y
    def __ne__(self, a):
        return self.x != a.x or self.y != a.y
    
    def __isub__(self, a):
        return self - a
    def __iadd__(self, a):
        return self + a
    def __imul__(self, a):
        return self * a
    def __idiv__(self, a):
        return self / a

    @staticmethod
    def from_map(a):
        return Point(a["x"], a["y"])
    @staticmethod
    def from_map_list(a):
        l = list()
        for i in a:
            l.append(Point.from_map(i))
        return l
    @staticmethod
    def to_string_list(a):
        l = list()
        for i in a:
            l.append(str(i))
        return l