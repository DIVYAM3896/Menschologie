class point:

    def __init__(self, x, y, Z):
        self.x = x
        self.y = y
        self.Z = Z

    def coordinates(self):
       # print(self.x, self.y, self.z)
        return (self.x,self.y,self.Z )

    def distance(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        z1 = self.Z
        z2 = other_point.Z
        return (((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z2 - z1) ** 2) ** 0.5)

    def manhatten(self, other_point):
        x1 = self.x
        x2 = other_point.x
        y1 = self.y
        y2 = other_point.y
        z1 = self.Z
        z2 = other_point.Z
        return (abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1))



a = point(10, 12, 20)
b = point(20, 30, 40)
c = a.coordinates()
print(a.distance(b))
print(c)


## extend class to work with 3d points
## make new class